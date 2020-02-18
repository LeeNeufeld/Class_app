import json # Import json function library
import urllib #Import Django URL function library

from django.shortcuts import render, redirect #import Django HTTP render and redirect functions
from django.http import HttpResponse # Import Django HTTPResponse function
from django.contrib import messages, auth # Import Message and authorizations from settings.py file
from django.contrib.auth import get_user_model #Import Get_user_model function from Django library
from django.contrib.auth.models import User #import the default Django user model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm # Import Form auths from settings.py file
from django.contrib.auth import update_session_auth_hash 
from django.db.models.functions import Log, Ntile # import calculation functions from Django Library
from django.conf import settings # Import config settings from settings.py file
from django.core.mail import send_mail # Import send email function from Django library
from django.db.models import F, Count, Max #Import counting queryset functions from Django Library
from django.db import connection # Import database connection from Settings.py file
from django.views.generic import ListView # Import Django listview function for leaderboard display
from django_tables2 import SingleTableView # import Django Table view function for leaderboard display
from itertools import chain # Import Chain function for queryset optimzation
from users.forms import CustomUserChangeForm, CustomUserCreationForm # Import custom forms from forms.py file
from response.models import CareResponses, FairResponses, LibResponses, LoyResponses, SanResponses, AuthResponses, Totals # import Leaderboard DB models
from questions.models import Questions #import Question DB model
from sentences.models import PartyReleases, Twitter, Sentences, NotStarted, InProgress, Classified, Undetermined, UserResponse # import DB sentence models
from users.models import CustomUser # Import DB customer user model
from users.tables import CareTable



User = get_user_model() # Function to access the custom user model globally across the app

# Edit profile view for editprofile.html
def editprofile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(  # Load the edit profile form using the current user instance
            request.POST, instance=request.user)
        if form.is_valid():  # Validate and save changes to profile
            form.save()
            return redirect('profile')

    else:
        form = CustomUserChangeForm(instance=request.user)
    args = {'form': form}
    return render(request, 'pages/editprofile.html', args) # return and render the change request

# View for index.html file
def index(request):
    return render(request, 'pages/index.html') #request and render Index page

# View for the CARE/HARM Classifier
def classifier(request):
    classifications = request.POST.get('classification') # request and post classification data to store to the DB
    question = Questions.objects.get(id='1') # request question from DB to store in the DB
    questionid = request.POST.get('questionid') #request and post the question id to store in the DB
    
    # request current user demographics to store data in the in_progress table
    user_id = request.user.id
    screen_name = request.user.screen_name
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    income = request.user.income
    ethncity = request.user.ethnicity
    nationality = request.user.nationality
    urbanization = request.user.urbanization
    religion = request.user.religion
    educational_attainment = request.user.education_attainment 

    # sentence pull queries
    # nsentences pulls a non classified sentence from the DB with the highest confidence score. This query is implemented if the csentences query does not find a sentence. 
    # csentences pulls a sentence from the DB that has been classified by a user that is not like the current user. This is done to ensure that the sentence is classified by users that are demographically different       
    nsentences = NotStarted.objects.raw("SELECT n.id, s.sentence FROM not_started AS n, sentences AS s WHERE n.sentenceid=s.id limit 1")
    csentences = InProgress.objects.only('sentence').exclude(userid = request.user.id)[:1]
    sentenceid = request.POST.get('sentenceid') # request and post the ID of the selected sentence to the DB

    # Condences the above definitions for simplified code
    context = {
        'questionid': questionid,
        'religion': religion,
        'urbanization': urbanization,
        'nationality': nationality,
        'ethncity': ethncity,
        'educational_attainment': educational_attainment,
        'income': income,
        'sentenceid': sentenceid,
        'nsentences': nsentences,
        'csentences': csentences,
        'question': question,
        'classifications': classifications,
        'user_id': user_id,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country,}
    
    # Validates the post request data and save to DB
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.POST.get('nsentence') or request.POST.get('csentence') and request.POST.get('classification'):
                post = InProgress(sentence=(nsentences, csentences), classification=classifications, userid=user_id, sentenceid=sentenceid,
                                    age=age, gender=gender, postal_code=postal_code, country=country, religion=religion, urbanization=urbanization, nationality=nationality, ethncity=ethncity, educational_attainment=educational_attainment, income=income, questionid=questionid)
                post2 = UserResponse(userid=user_id, sentenceid=sentenceid, classification=classifications)
                post2.userid = request.POST.get('userid')
                post2.sentenceid = request.POST.get('sentenceid')
                post2.classification = request.POST.get('classification')
                post2.save()
                post.sentenceid = request.POST.get('sentenceid')
                post.questionid = request.POST.get('questionid')
                post.religion = request.POST.get('religion')
                post.urbanization = request.POST.get('urbanization')
                post.nationality = request.POST.get('nationality')
                post.ethncity = request.POST.get('ethncity')
                post.educational_attainment = request.POST.get('educational_attainment')
                post.income = request.POST.get('income')
                post.sentence = request.POST.get('nsentence','csentence')
                post.classification = request.POST.get('classification')
                post.userId = request.POST.get('userid')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()

                cursor = connection.cursor()# opens a direct connection to interact with the DB to complete complex queries

                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                cursor.execute("update response_totals set screen_name = sname.screen_name from (select id, screen_name from users_customuser ) as sname where sname.id  = response_totals.userid")
                cursor.execute("insert into classified(sentenceid,classification)(SELECT sentenceid, classification FROM in_progress group by sentenceid, classification having count(sentence) >= 2)") # updates the classified table where a sentnce has been classified the same twice by different users to give that sentence an offical classification
                cursor.execute("DELETE FROM in_progress USING classified WHERE in_progress.sentenceid = classified.sentenceid") # removes the sentence from the in_progress table once it has been placed in the classified table to stop it from be classified again
                cursor.execute("insert into undetermined (sentenceid)(SELECT sentenceid FROM in_progress group by sentenceid having count(sentence) >= 2)") # updates the undetermined table where a sentence has been classified differently by 2 different users to allow the sentence to be reviewed to see the resoning for the inconsistantcy
                cursor.execute("DELETE FROM in_progress USING undetermined WHERE in_progress.sentenceid = undetermined.sentenceid") # removes the sentence from the in_progress table when it is added to the undetermined table to not allow continuing classifications
                cursor.execute("DELETE FROM not_started USING in_progress WHERE not_started.sentenceid = in_progress.sentenceid")# removes the sentence from the not_started table once a user classifies it and it is moved to the in_progress table to allow other users to classifiy the sentence based of other user classifications
                connection.commit()
                return render(request, 'pages/classifier.html', context)
        else:
            return render(request, 'pages/classifier.html', context)
    else:
        return render(request, 'pages/classifier.html', context)


def classifierfairness(request):
    classifications = request.POST.get('classification') # request and post classification data to store to the DB
    questionf = Questions.objects.get(id='2')
    questionid = request.POST.get('questionid') #request and post the question id to store in the DB
    # request current user demographics to store data in the in_progress table
    user_id = request.user.id
    screen_name = request.user.screen_name
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    income = request.user.income
    ethncity = request.user.ethnicity
    nationality = request.user.nationality
    urbanization = request.user.urbanization
    religion = request.user.religion
    educational_attainment = request.user.education_attainment 
    # sentence pull queries
    # nsentences pulls a non classified sentence from the DB with the highest confidence score. This query is implemented if the csentences query does not find a sentence. 
    # csentences pulls a sentence from the DB that has been classified by a user that is not like the current user. This is done to ensure that the sentence is classified by users that are demographically different       
    nsentences = NotStarted.objects.raw("SELECT n.id, s.sentence FROM not_started AS n, sentences AS s WHERE n.sentenceid=s.id limit 1 ")
    csentences = InProgress.objects.only('sentence').exclude(userid = request.user.id)[:1]
    sentenceid = request.POST.get('sentenceid') # request and post the ID of the selected sentence to the DB
    # condenses the above defintions to simplefy the code when defining the render object below
    contextf = {
        'questionid': questionid,
        'religion': religion,
        'urbanization': urbanization,
        'nationality': nationality,
        'ethncity': ethncity,
        'educational_attainment': educational_attainment,
        'income': income,
        'sentenceid': sentenceid,
        'nsentences': nsentences,
        'csentences': csentences,
        'question': questionf,
        'classifications': classifications,
        'user_id': user_id,
        'screen_name': screen_name,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country
    }
    if request.method == 'POST':
        if request.user.is_authenticated:# authenticates the post data to check if valid before saving to the DB
             if request.POST.get('nsentence') or request.POST.get('csentence') and request.POST.get('classification'): # this defines the varibles present to inciate the save
                 # post defines the information being saved to the InProgress table in the DB
                post = InProgress(sentence=(nsentences, csentences), classification=classifications, userid=user_id, sentenceid=sentenceid,
                                    age=age, gender=gender, postal_code=postal_code, country=country, religion=religion, urbanization=urbanization, nationality=nationality, ethncity=ethncity, educational_attainment=educational_attainment, income=income, questionid=questionid)
                #post2 defines the data being saved to the UserResponse table in the DB
                post2 = UserResponse(userid=user_id, sentenceid=sentenceid, classification=classifications)
                #gets and saves the values found in the inputs on the classifier page
                post2.userid = request.POST.get('userid')
                post2.sentenceid = request.POST.get('sentenceid')
                post2.classification = request.POST.get('classification')
                post2.save()
                post.sentenceid = request.POST.get('sentenceid')
                post.questionid = request.POST.get('questionid')
                post.religion = request.POST.get('religion')
                post.urbanization = request.POST.get('urbanization')
                post.nationality = request.POST.get('nationality')
                post.ethncity = request.POST.get('ethncity')
                post.educational_attainment = request.POST.get('educational_attainment')
                post.income = request.POST.get('income')
                post.sentence = request.POST.get('nsentence','csentence')
                post.classification = request.POST.get('classification')
                post.userId = request.POST.get('userid')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()

                cursor = connection.cursor()# opens a direct connection to interact with the DB to complete complex queries

                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                cursor.execute("update response_totals set screen_name = sname.screen_name from (select id, screen_name from users_customuser ) as sname where sname.id  = response_totals.userid")
                cursor.execute("insert into classified(sentenceid,classification)(SELECT sentenceid, classification FROM in_progress group by sentenceid, classification having count(sentence) >= 2)") # updates the classified table where a sentnce has been classified the same twice by different users to give that sentence an offical classification
                cursor.execute("DELETE FROM in_progress USING classified WHERE in_progress.sentenceid = classified.sentenceid") # removes the sentence from the in_progress table once it has been placed in the classified table to stop it from be classified again
                cursor.execute("insert into undetermined (sentenceid)(SELECT sentenceid FROM in_progress group by sentenceid having count(sentence) >= 2)") # updates the undetermined table where a sentence has been classified differently by 2 different users to allow the sentence to be reviewed to see the resoning for the inconsistantcy
                cursor.execute("DELETE FROM in_progress USING undetermined WHERE in_progress.sentenceid = undetermined.sentenceid") # removes the sentence from the in_progress table when it is added to the undetermined table to not allow continuing classifications
                cursor.execute("DELETE FROM not_started USING in_progress WHERE not_started.sentenceid = in_progress.sentenceid")# removes the sentence from the not_started table once a user classifies it and it is moved to the in_progress table to allow other users to classifiy the sentence based of other user classifications
                connection.commit()
                return render(request, 'pages/classifier-fairness.html', contextf)
        else:
            return render(request, 'pages/classifier-fairness.html', contextf)
    else:
        return render(request, 'pages/classifier-fairness.html', contextf)


def classifierloyalty(request):
    classifications = request.POST.get('classification') # request and post classification data to store to the DB
    questionl = Questions.objects.get(id='3')
    questionid = request.POST.get('questionid') #request and post the question id to store in the DB
    # request current user demographics to store data in the in_progress table
    user_id = request.user.id
    screen_name = request.user.screen_name
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    income = request.user.income
    ethncity = request.user.ethnicity
    nationality = request.user.nationality
    urbanization = request.user.urbanization
    religion = request.user.religion
    educational_attainment = request.user.education_attainment 
    # sentence pull queries
    # nsentences pulls a non classified sentence from the DB with the highest confidence score. This query is implemented if the csentences query does not find a sentence. 
    # csentences pulls a sentence from the DB that has been classified by a user that is not like the current user. This is done to ensure that the sentence is classified by users that are demographically different       
    nsentences = NotStarted.objects.raw("SELECT n.id, s.sentence FROM not_started AS n, sentences AS s WHERE n.sentenceid=s.id limit 1")
    csentences = InProgress.objects.only('sentence').exclude(userid = request.user.id)[:1]
    sentenceid = request.POST.get('sentenceid') # request and post the ID of the selected sentence to the DB
    # condenses the above defintions to simplefy the code when defining the render object below
    contextl = {
        'questionid': questionid,
        'religion': religion,
        'urbanization': urbanization,
        'nationality': nationality,
        'ethncity': ethncity,
        'educational_attainment': educational_attainment,
        'income': income,
        'sentenceid': sentenceid,
        'nsentences': nsentences,
        'csentences': csentences,
        'question': questionl,
        'classifications': classifications,
        'user_id': user_id,
        'screen_name': screen_name,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
         if request.POST.get('nsentence') or request.POST.get('csentence') and request.POST.get('classification'): # this defines the varibles present to inciate the save
                 # post defines the information being saved to the InProgress table in the DB
                post = InProgress(sentence=(nsentences, csentences), classification=classifications, userid=user_id, sentenceid=sentenceid,
                                    age=age, gender=gender, postal_code=postal_code, country=country, religion=religion, urbanization=urbanization, nationality=nationality, ethncity=ethncity, educational_attainment=educational_attainment, income=income, questionid=questionid)
                #post2 defines the data being saved to the UserResponse table in the DB
                post2 = UserResponse(userid=user_id, sentenceid=sentenceid, classification=classifications)
                #gets and saves the values found in the inputs on the classifier page
                post2.userid = request.POST.get('userid')
                post2.sentenceid = request.POST.get('sentenceid')
                post2.classification = request.POST.get('classification')
                post2.save()
                post.sentenceid = request.POST.get('sentenceid')
                post.questionid = request.POST.get('questionid')
                post.religion = request.POST.get('religion')
                post.urbanization = request.POST.get('urbanization')
                post.nationality = request.POST.get('nationality')
                post.ethncity = request.POST.get('ethncity')
                post.educational_attainment = request.POST.get('educational_attainment')
                post.income = request.POST.get('income')
                post.sentence = request.POST.get('nsentence','csentence')
                post.classification = request.POST.get('classification')
                post.userId = request.POST.get('userid')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()
                cursor = connection.cursor()
                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                cursor.execute("update response_totals set screen_name = sname.screen_name from (select id, screen_name from users_customuser ) as sname where sname.id  = response_totals.userid")
                cursor.execute("insert into classified(sentenceid,classification)(SELECT sentenceid, classification FROM in_progress group by sentenceid, classification having count(sentence) >= 2)") # updates the classified table where a sentnce has been classified the same twice by different users to give that sentence an offical classification
                cursor.execute("DELETE FROM in_progress USING classified WHERE in_progress.sentenceid = classified.sentenceid") # removes the sentence from the in_progress table once it has been placed in the classified table to stop it from be classified again
                cursor.execute("insert into undetermined (sentenceid)(SELECT sentenceid FROM in_progress group by sentenceid having count(sentence) >= 2)") # updates the undetermined table where a sentence has been classified differently by 2 different users to allow the sentence to be reviewed to see the resoning for the inconsistantcy
                cursor.execute("DELETE FROM in_progress USING undetermined WHERE in_progress.sentenceid = undetermined.sentenceid") # removes the sentence from the in_progress table when it is added to the undetermined table to not allow continuing classifications
                cursor.execute("DELETE FROM not_started USING in_progress WHERE not_started.sentenceid = in_progress.sentenceid")# removes the sentence from the not_started table once a user classifies it and it is moved to the in_progress table to allow other users to classifiy the sentence based of other user classifications
                connection.commit()
                return render(request, 'pages/classifier-loyalty.html', contextl)
        else:
            return render(request, 'pages/classifier-loyalty.html', contextl)
    else:
        return render(request, 'pages/classifier-loyalty.html', contextl)


def classifierauthority(request):
    classifications = request.POST.get('classification') # request and post classification data to store to the DB
    questiona = Questions.objects.get(id='4')
    questionid = request.POST.get('questionid') #request and post the question id to store in the DB
    user_id = request.user.id
    screen_name = request.user.screen_name
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    income = request.user.income
    ethncity = request.user.ethnicity
    nationality = request.user.nationality
    urbanization = request.user.urbanization
    religion = request.user.religion
    educational_attainment = request.user.education_attainment 
    # sentence pull queries
    # nsentences pulls a non classified sentence from the DB with the highest confidence score. This query is implemented if the csentences query does not find a sentence. 
    # csentences pulls a sentence from the DB that has been classified by a user that is not like the current user. This is done to ensure that the sentence is classified by users that are demographically different       
    nsentences = NotStarted.objects.raw("SELECT n.id, s.sentence FROM not_started AS n, sentences AS s WHERE n.sentenceid=s.id limit 1")
    csentences = InProgress.objects.only('sentence').exclude(userid = request.user.id)[:1]
    sentenceid = request.POST.get('sentenceid') # request and post the ID of the selected sentence to the DB
    # condenses the above defintions to simplefy the code when defining the render object below
    contexta = {
        'questionid': questionid,
        'religion': religion,
        'urbanization': urbanization,
        'nationality': nationality,
        'ethncity': ethncity,
        'educational_attainment': educational_attainment,
        'income': income,
        'sentenceid': sentenceid,
        'nsentences': nsentences,
        'csentences': csentences,
        'question': questiona,
        'classifications': classifications,
        'user_id': user_id,
        'screen_name': screen_name,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
         if request.POST.get('nsentence') or request.POST.get('csentence') and request.POST.get('classification'): # this defines the varibles present to inciate the save
                 # post defines the information being saved to the InProgress table in the DB
                post = InProgress(sentence=(nsentences, csentences), classification=classifications, userid=user_id, sentenceid=sentenceid,
                                    age=age, gender=gender, postal_code=postal_code, country=country, religion=religion, urbanization=urbanization, nationality=nationality, ethncity=ethncity, educational_attainment=educational_attainment, income=income, questionid=questionid)
                #post2 defines the data being saved to the UserResponse table in the DB
                post2 = UserResponse(userid=user_id, sentenceid=sentenceid, classification=classifications)
                #gets and saves the values found in the inputs on the classifier page
                post2.userid = request.POST.get('userid')
                post2.sentenceid = request.POST.get('sentenceid')
                post2.classification = request.POST.get('classification')
                post2.save()
                post.sentenceid = request.POST.get('sentenceid')
                post.questionid = request.POST.get('questionid')
                post.religion = request.POST.get('religion')
                post.urbanization = request.POST.get('urbanization')
                post.nationality = request.POST.get('nationality')
                post.ethncity = request.POST.get('ethncity')
                post.educational_attainment = request.POST.get('educational_attainment')
                post.income = request.POST.get('income')
                post.sentence = request.POST.get('nsentence','csentence')
                post.classification = request.POST.get('classification')
                post.userId = request.POST.get('userid')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()
                cursor = connection.cursor()
                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                cursor.execute("update response_totals set screen_name = sname.screen_name from (select id, screen_name from users_customuser ) as sname where sname.id  = response_totals.userid")
                cursor.execute("insert into classified(sentenceid,classification)(SELECT sentenceid, classification FROM in_progress group by sentenceid, classification having count(sentence) >= 2)") # updates the classified table where a sentnce has been classified the same twice by different users to give that sentence an offical classification
                cursor.execute("DELETE FROM in_progress USING classified WHERE in_progress.sentenceid = classified.sentenceid") # removes the sentence from the in_progress table once it has been placed in the classified table to stop it from be classified again
                cursor.execute("insert into undetermined (sentenceid)(SELECT sentenceid FROM in_progress group by sentenceid having count(sentence) >= 2)") # updates the undetermined table where a sentence has been classified differently by 2 different users to allow the sentence to be reviewed to see the resoning for the inconsistantcy
                cursor.execute("DELETE FROM in_progress USING undetermined WHERE in_progress.sentenceid = undetermined.sentenceid") # removes the sentence from the in_progress table when it is added to the undetermined table to not allow continuing classifications
                cursor.execute("DELETE FROM not_started USING in_progress WHERE not_started.sentenceid = in_progress.sentenceid")# removes the sentence from the not_started table once a user classifies it and it is moved to the in_progress table to allow other users to classifiy the sentence based of other user classifications
                connection.commit()
                return render(request, 'pages/classifier-authority.html', contexta)
        else:
            return render(request, 'pages/classifier-authority.html', contexta)
    else:
        return render(request, 'pages/classifier-authority.html', contexta)


def classifiersanctity(request):
    classifications = request.POST.get('classification') # request and post classification data to store to the DB
    questionS = Questions.objects.get(id='5')
    questionid = request.POST.get('questionid') #request and post the question id to store in the DB
    user_id = request.user.id
    screen_name = request.user.screen_name
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    income = request.user.income
    ethncity = request.user.ethnicity
    nationality = request.user.nationality
    urbanization = request.user.urbanization
    religion = request.user.religion
    educational_attainment = request.user.education_attainment 
    # sentence pull queries
    # nsentences pulls a non classified sentence from the DB with the highest confidence score. This query is implemented if the csentences query does not find a sentence. 
    # csentences pulls a sentence from the DB that has been classified by a user that is not like the current user. This is done to ensure that the sentence is classified by users that are demographically different       
    nsentences = NotStarted.objects.raw("SELECT n.id, s.sentence FROM not_started AS n, sentences AS s WHERE n.sentenceid=s.id limit 1")
    csentences = InProgress.objects.only('sentence').exclude(userid = request.user.id)[:1]
    sentenceid = request.POST.get('sentenceid') # request and post the ID of the selected sentence to the DB
    # condenses the above defintions to simplefy the code when defining the render object below
    contextS = {
        'questionid': questionid,
        'religion': religion,
        'urbanization': urbanization,
        'nationality': nationality,
        'ethncity': ethncity,
        'educational_attainment': educational_attainment,
        'income': income,
        'sentenceid': sentenceid,
        'nsentences': nsentences,
        'csentences': csentences,
        'question': questionS,
        'classifications': classifications,
        'user_id': user_id,
        'screen_name': screen_name,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
         if request.POST.get('nsentence') or request.POST.get('csentence') and request.POST.get('classification'): # this defines the varibles present to inciate the save
                 # post defines the information being saved to the InProgress table in the DB
                post = InProgress(sentence=(nsentences, csentences), classification=classifications, userid=user_id, sentenceid=sentenceid,
                                    age=age, gender=gender, postal_code=postal_code, country=country, religion=religion, urbanization=urbanization, nationality=nationality, ethncity=ethncity, educational_attainment=educational_attainment, income=income, questionid=questionid)
                #post2 defines the data being saved to the UserResponse table in the DB
                post2 = UserResponse(userid=user_id, sentenceid=sentenceid, classification=classifications)
                #gets and saves the values found in the inputs on the classifier page
                post2.userid = request.POST.get('userid')
                post2.sentenceid = request.POST.get('sentenceid')
                post2.classification = request.POST.get('classification')
                post2.save()
                post.sentenceid = request.POST.get('sentenceid')
                post.questionid = request.POST.get('questionid')
                post.religion = request.POST.get('religion')
                post.urbanization = request.POST.get('urbanization')
                post.nationality = request.POST.get('nationality')
                post.ethncity = request.POST.get('ethncity')
                post.educational_attainment = request.POST.get('educational_attainment')
                post.income = request.POST.get('income')
                post.sentence = request.POST.get('nsentence','csentence')
                post.classification = request.POST.get('classification')
                post.userId = request.POST.get('userid')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()
                cursor = connection.cursor()
                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                cursor.execute("update response_totals set screen_name = sname.screen_name from (select id, screen_name from users_customuser ) as sname where sname.id  = response_totals.userid")
                cursor.execute("insert into classified(sentenceid,classification)(SELECT sentenceid, classification FROM in_progress group by sentenceid, classification having count(sentence) >= 2)") # updates the classified table where a sentnce has been classified the same twice by different users to give that sentence an offical classification
                cursor.execute("DELETE FROM in_progress USING classified WHERE in_progress.sentenceid = classified.sentenceid") # removes the sentence from the in_progress table once it has been placed in the classified table to stop it from be classified again
                cursor.execute("insert into undetermined (sentenceid)(SELECT sentenceid FROM in_progress group by sentenceid having count(sentence) >= 2)") # updates the undetermined table where a sentence has been classified differently by 2 different users to allow the sentence to be reviewed to see the resoning for the inconsistantcy
                cursor.execute("DELETE FROM in_progress USING undetermined WHERE in_progress.sentenceid = undetermined.sentenceid") # removes the sentence from the in_progress table when it is added to the undetermined table to not allow continuing classifications
                cursor.execute("DELETE FROM not_started USING in_progress WHERE not_started.sentenceid = in_progress.sentenceid")# removes the sentence from the not_started table once a user classifies it and it is moved to the in_progress table to allow other users to classifiy the sentence based of other user classifications
                connection.commit()
                return render(request, 'pages/classifier-sanctity.html', contextS)
        else:
            return render(request, 'pages/classifier-sanctity.html', contextS)
    else:
        return render(request, 'pages/classifier-sanctity.html', contextS)


def classifierliberty(request):
    classifications = request.POST.get('classification') # request and post classification data to store to the DB
    questionL = Questions.objects.get(id='6')
    questionid = request.POST.get('questionid') #request and post the question id to store in the DB
    user_id = request.user.id
    screen_name = request.user.screen_name
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    income = request.user.income
    ethncity = request.user.ethnicity
    nationality = request.user.nationality
    urbanization = request.user.urbanization
    religion = request.user.religion
    educational_attainment = request.user.education_attainment 
    # sentence pull queries
    # nsentences pulls a non classified sentence from the DB with the highest confidence score. This query is implemented if the csentences query does not find a sentence. 
    # csentences pulls a sentence from the DB that has been classified by a user that is not like the current user. This is done to ensure that the sentence is classified by users that are demographically different       
    nsentences = NotStarted.objects.raw("SELECT n.id, s.sentence FROM not_started AS n, sentences AS s WHERE n.sentenceid=s.id limit 1")
    csentences = InProgress.objects.only('sentence').exclude(userid = request.user.id)[:1]
    sentenceid = request.POST.get('sentenceid') # request and post the ID of the selected sentence to the DB
    # condenses the above defintions to simplefy the code when defining the render object below
    contextL = {
        'questionid': questionid,
        'religion': religion,
        'urbanization': urbanization,
        'nationality': nationality,
        'ethncity': ethncity,
        'educational_attainment': educational_attainment,
        'income': income,
        'sentenceid': sentenceid,
        'nsentences': nsentences,
        'csentences': csentences,
        'question': questionL,
        'classifications': classifications,
        'user_id': user_id,
        'screen_name': screen_name,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
         if request.POST.get('nsentence') or request.POST.get('csentence') and request.POST.get('classification'): # this defines the varibles present to inciate the save
                 # post defines the information being saved to the InProgress table in the DB
                post = InProgress(sentence=(nsentences, csentences), classification=classifications, userid=user_id, sentenceid=sentenceid,
                                    age=age, gender=gender, postal_code=postal_code, country=country, religion=religion, urbanization=urbanization, nationality=nationality, ethncity=ethncity, educational_attainment=educational_attainment, income=income, questionid=questionid)
                #post2 defines the data being saved to the UserResponse table in the DB
                post2 = UserResponse(userid=user_id, sentenceid=sentenceid, classification=classifications)
                #gets and saves the values found in the inputs on the classifier page
                post2.userid = request.POST.get('userid')
                post2.sentenceid = request.POST.get('sentenceid')
                post2.classification = request.POST.get('classification')
                post2.save()
                post.sentenceid = request.POST.get('sentenceid')
                post.questionid = request.POST.get('questionid')
                post.religion = request.POST.get('religion')
                post.urbanization = request.POST.get('urbanization')
                post.nationality = request.POST.get('nationality')
                post.ethncity = request.POST.get('ethncity')
                post.educational_attainment = request.POST.get('educational_attainment')
                post.income = request.POST.get('income')
                post.sentence = request.POST.get('nsentence','csentence')
                post.classification = request.POST.get('classification')
                post.userId = request.POST.get('userid')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()
                cursor = connection.cursor()
                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                cursor.execute("update response_totals set screen_name = sname.screen_name from (select id, screen_name from users_customuser ) as sname where sname.id  = response_totals.userid")
                cursor.execute("insert into classified(sentenceid,classification)(SELECT sentenceid, classification FROM in_progress group by sentenceid, classification having count(sentence) >= 2)") # updates the classified table where a sentnce has been classified the same twice by different users to give that sentence an offical classification
                cursor.execute("DELETE FROM in_progress USING classified WHERE in_progress.sentenceid = classified.sentenceid") # removes the sentence from the in_progress table once it has been placed in the classified table to stop it from be classified again
                cursor.execute("insert into undetermined (sentenceid)(SELECT sentenceid FROM in_progress group by sentenceid having count(sentence) >= 2)") # updates the undetermined table where a sentence has been classified differently by 2 different users to allow the sentence to be reviewed to see the resoning for the inconsistantcy
                cursor.execute("DELETE FROM in_progress USING undetermined WHERE in_progress.sentenceid = undetermined.sentenceid") # removes the sentence from the in_progress table when it is added to the undetermined table to not allow continuing classifications
                cursor.execute("DELETE FROM not_started USING in_progress WHERE not_started.sentenceid = in_progress.sentenceid")# removes the sentence from the not_started table once a user classifies it and it is moved to the in_progress table to allow other users to classifiy the sentence based of other user classifications
                connection.commit()
                return render(request, 'pages/classifier-liberty.html', contextL)
        else:
            return render(request, 'pages/classifier-liberty.html', contextL)
    else:
        return render(request, 'pages/classifier-liberty.html', contextL)

# View for the login.html file
def login(request):
    #statement to authenticate username and password to prevent users that have not registered from logging in
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None: # if user exists then login
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('splash')
        else: # if user not exists login fails
            messages.error(request, 'User not found')
            return redirect('login')

    else:
        return render(request, 'pages/login.html')

# Process logout request and terminate session
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')

# view for register.html
def register(request, *args, **kwargs):
    # Define and post new user data to be saved in the Users table
    if request.method == 'POST':
        gender = request.POST['gender']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        email = request.POST['username']
        screen_name = request.POST['screen_name']
        age = request.POST['age']
        country = request.POST['country']
        postal_code = request.POST['postal_code']
        education_attainment = request.POST['education_attainment']
        income = request.POST['income']
        urbanization = request.POST['urbanization']
        ethnicity = request.POST['ethnicity']
        nationality = request.POST['nationality']
        religion = request.POST['religion']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if username already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Username already used')
            return redirect('register')
        else: # check if user email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already used')
                return redirect('register')
            else: # saves the new user data to DB
                user = User.objects.create_user(first_name=first_name, last_name=last_name, religion=religion, urbanization=urbanization, email=email, screen_name=screen_name, username=email, password=password, age=age,
                                                country=country, postal_code=postal_code, gender=gender, nationality=nationality, education_attainment=education_attainment, income=income, ethnicity=ethnicity)
                # implements google recaptcha protocol to prevent "bots" from accessing the app
                def form_valid(self, form):

                    # get the token submitted in the form to authicate
                    recaptcha_response = self.request.POST.get(
                        'g-recaptcha-response')
                    url = 'https://www.google.com/recaptcha/api/siteverify'
                    payload = {
                        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                        'response': recaptcha_response
                    }
                    data = urllib.parse.urlencode(payload).encode()
                    req = urllib.request.Request(url, data=data)

                    # verify the token submitted with the form is valid
                    response = urllib.request.urlopen(req)
                    result = json.loads(response.read().decode())

                    # result will be a dict containing 'success' and 'action'.
                    # it is important to verify both

                    # make sure action matches the one from your template
                    if (not result['success']) or (not result['action'] == 'signup'):
                        messages.error(
                            self.request, 'Invalid reCAPTCHA. Please try again.')
                        return super().form_invalid(form)
                user.save(*args, **kwargs)
                # Generates and sends email to the new user to confirm registration
                subject = 'Thank you for registering!'
                message = 'Welcome to the Moral Class App! You have been registered and are ready to start classifying sentences. Thank you from RA2!'
                from_email = settings.EMAIL_HOST_USER
                to_email = [user.email]
                send_mail(subject, message, from_email,
                          to_email, fail_silently=True)

                messages.success(request, 'Your profile has been updated')
                return redirect('tutorial')
    else:
        return render(request, 'pages/register.html', {'site_key': settings.RECAPTCHA_SITE_KEY})

# views to render the tutorial pages
def tutorial(request):
    return render(request, 'pages/tutorial.html')


def tutorial2(request):
    return render(request, 'pages/tutorial2.html')

# view for user test page when built
def test(request):
    return render(request, 'pages/test.html')

# view for the dashboard.html
def dashboard(request):
    return render(request, 'pages/dashboard.html')

# view for the tutorial dashboard
def dashtutorial(request):
    return render(request, 'pages/dashtutorial.html')

# view for the user profile page
def profile(request):
    args = {'user': request.user} # pulls the current user data from the DB
    return render(request, 'pages/profile.html', args)

# view for the splash.html page
def splash(request):
    return render(request, 'pages/splash.html')

# view for the changepassword.html
def change_password(request):
    # request and validate the change password form
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user) # pulls the change form from the forms.py file to allow user to change password
        if form.is_valid():
            form.save() # checks if the form is valid and updates the users password
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user) # if submission is not valid and new blank form is rendered. 
    args = {'form': form}
    return render(request, 'pages/change_password.html', args)

# view for leaderboard.html These queries will change to support the new classifier and table structure. currently these are based on the previous struture and do not function properly
def leaderboard(request):
    totalleads = Totals.objects.raw("SELECT id, total, screen_name FROM response_totals WHERE total = ( SELECT MAX (total) FROM response_totals) LIMIT 5;")
    careleads = Totals.objects.raw("SELECT id, care_harm, screen_name FROM response_totals WHERE care_harm = ( SELECT MAX (care_harm) FROM response_totals) LIMIT 5;")
    libleads = Totals.objects.raw("SELECT id, liberty_oppression, screen_name FROM response_totals WHERE liberty_oppression = ( SELECT MAX (liberty_oppression) FROM response_totals) LIMIT 5;")
    loyleads = Totals.objects.raw("SELECT id, loyalty_betrayal, screen_name FROM response_totals WHERE loyalty_betrayal = ( SELECT MAX (loyalty_betrayal) FROM response_totals) LIMIT 5;")
    sanleads = Totals.objects.raw("SELECT id, sanctity_degradation, screen_name FROM response_totals WHERE sanctity_degradation = ( SELECT MAX (sanctity_degradation) FROM response_totals) LIMIT 5;")
    authleads = Totals.objects.raw("SELECT id, authority_subversion, screen_name FROM response_totals WHERE authority_subversion = ( SELECT MAX (authority_subversion) FROM response_totals) LIMIT 5;")
    fairleads = Totals.objects.raw("SELECT id, fairness_cheating, screen_name FROM response_totals WHERE fairness_cheating = ( SELECT MAX (fairness_cheating) FROM response_totals) LIMIT 5;")


    args = {'totalleads': totalleads, 'careleads': careleads, 'libleads': libleads, 'loyleads':loyleads, 'sanleads':sanleads, 'authleads':authleads, 'fairleads':fairleads}
    return render(request, 'pages/leaderboard.html', args)
