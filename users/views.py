import json
import urllib

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F, Count, Max
from django.db import connection 
from django.views.generic import ListView
from django_tables2 import SingleTableView
from itertools import chain
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from response.models import CareResponses, FairResponses, LibResponses, LoyResponses, SanResponses, AuthResponses, Totals
from questions.models import Questions
from sentences.models import ClassSentence
from users.models import CustomUser
from users.tables import CareTable

User = get_user_model()



def editprofile (request):
        if request.method == 'POST':
                form = CustomUserChangeForm(request.POST, instance=request.user)
                if form.is_valid():
                        form.save()
                        return redirect ('profile')
               
        else:
                form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'pages/editprofile.html', args)


def index(request):
 return render(request, 'pages/index.html')

def classifier(request):
    responses = request.POST.get('response')
    question = Questions.objects.get(id='1')
    random_objects =ClassSentence.objects.raw("SELECT * FROM class_sentence WHERE NOT EXISTS (SELECT * FROM response_careresponses WHERE class_sentence.sentence = response_careresponses.sentence) ORDER BY -LOG(1.0 - random()) / weight LIMIT 1")
    user_id = request.user.id
    screen_name = request.user.screen_name    
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    context = {
        'random_objects':random_objects,
        'question':question,
        'responses':responses,
        'user_id': user_id,
        'screen_name':screen_name,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country,

    }
    if request.method =='POST':
        if request.user.is_authenticated:
            if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                post=CareResponses(question=question, sentence=random_objects, response=responses, userid=user_id, screen_name=screen_name, age=age, gender=gender, postal_code=postal_code, country=country)
                post.question=request.POST.get('question')
                post.sentence=request.POST.get('random_object')
                post.response=request.POST.get('response')
                post.userId = request.POST.get('userid')
                post.screen_name = request.POST.get('screen_name')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()
                
                cursor = connection.cursor()
                cursor.execute("update response_totals set care_harm = x.result from (select userid, count(*) as result from response_careresponses group by response_careresponses.userid) x where x.userid = response_totals.userid")
                cursor.execute("update response_totals set care_harm_yes = x.result from (select userid, count(*) as result from response_careresponses where response = 'Yes' group by response_careresponses.userid) x where x.userid = response_totals.userid")
                cursor.execute("update response_totals set care_harm_no = x.result from (select userid, count(*) as result from response_careresponses where response = 'No' group by response_careresponses.userid) x where x.userid = response_totals.userid")
                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                cursor.execute("update class_sentence as cs set weight = (weight + 1) from response_careresponses as cr where cs.sentence = cr.sentence AND cr.response='Yes'")
                connection.commit()
                return render(request, 'pages/classifier.html', context)
        else:
            return render(request, 'pages/classifier.html', context)
    else:
        return render(request, 'pages/classifier.html', context)


def classifierfairness (request):
        responses = request.POST.get('response')
        questionf = Questions.objects.get(id='2')
        random_objects =ClassSentence.objects.raw("SELECT * FROM class_sentence WHERE NOT EXISTS (SELECT * FROM response_fairresponses WHERE class_sentence.sentence = response_fairresponses.sentence) ORDER BY -LOG(1.0 - random()) / weight LIMIT 1")
        user_id = request.user.id
        screen_name = request.user.screen_name
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextf = {
                'random_objects':random_objects,
                'question':questionf,
                'responses':responses,
                'user_id': user_id,
                'screen_name':screen_name,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=FairResponses(question=questionf, sentence=random_objects, response=responses, userid=user_id, screen_name=screen_name, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userid')
                                post.screen_name = request.POST.get('screen_name')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                cursor = connection.cursor()
                                cursor.execute("update response_totals set fairness_cheating = x.result from (select userid, count(*) as result from response_fairresponses group by response_fairresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set fairness_cheating_yes = x.result from (select userid, count(*) as result from response_fairresponses where response = 'Yes' group by response_fairresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set fairness_cheating_no = x.result from (select userid, count(*) as result from response_fairresponses where response = 'No' group by response_fairresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                                cursor.execute("update class_sentence as cs set weight = (weight + 1) from response_fairresponses as fr where cs.sentence = fr.sentence AND fr.response='Yes'")
                                connection.commit()
                                return render(request, 'pages/classifier-fairness.html', contextf)
                else:
                        return render(request, 'pages/classifier-fairness.html', contextf)
        else:
                return render(request, 'pages/classifier-fairness.html', contextf)

def classifierloyalty (request):
        responses = request.POST.get('response')
        questionl = Questions.objects.get(id='3')
        random_objects =ClassSentence.objects.raw("SELECT * FROM class_sentence WHERE NOT EXISTS (SELECT * FROM response_loyresponses WHERE class_sentence.sentence = response_loyresponses.sentence) ORDER BY -LOG(1.0 - random()) / weight LIMIT 1")
        user_id = request.user.id
        screen_name = request.user.screen_name
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextl = {
                'random_objects':random_objects,
                'question':questionl,
                'responses':responses,
                'user_id': user_id,
                'screen_name':screen_name,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=LoyResponses(question=questionl, sentence=random_objects, response=responses, userid=user_id, screen_name=screen_name, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userid')
                                post.screen_name = request.POST.get('screen_name')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                cursor = connection.cursor()
                                cursor.execute("update response_totals set loyalty_betrayal = x.result from (select userid, count(*) as result from response_loyresponses group by response_loyresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set loyalty_betrayal_yes = x.result from (select userid, count(*) as result from response_loyresponses where response = 'Yes' group by response_loyresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set loyalty_betrayal_no = x.result from (select userid, count(*) as result from response_loyresponses where response = 'No' group by response_loyresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                                cursor.execute("update class_sentence as cs set weight = (weight + 1) from response_loyresponses as yr where cs.sentence = yr.sentence AND yr.response='Yes'")
                                connection.commit()
                                return render(request, 'pages/classifier-loyalty.html', contextl)
                else:
                        return render(request, 'pages/classifier-loyalty.html', contextl)
        else:
                return render(request, 'pages/classifier-loyalty.html', contextl)

def classifierauthority (request):
        responses = request.POST.get('response')
        questiona = Questions.objects.get(id='4')
        random_objects =ClassSentence.objects.raw("SELECT * FROM class_sentence WHERE NOT EXISTS (SELECT * FROM response_authresponses WHERE class_sentence.sentence = response_authresponses.sentence) ORDER BY -LOG(1.0 - random()) / weight LIMIT 1")
        user_id = request.user.id
        screen_name = request.user.screen_name
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contexta = {
                'random_objects':random_objects,
                'question':questiona,
                'responses':responses,
                'user_id': user_id,
                'screen_name':screen_name,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=AuthResponses(question=questiona, sentence=random_objects, response=responses, userid=user_id, screen_name=screen_name, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userid')
                                post.screen_name = request.POST.get('screen_name')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                cursor = connection.cursor()
                                cursor.execute("update response_totals set authority_subversion = x.result from (select userid, count(*) as result from response_authresponses group by response_authresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set authority_subversion_yes = x.result from (select userid, count(*) as result from response_authresponses where response = 'Yes' group by response_authresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set authority_subversion_no = x.result from (select userid, count(*) as result from response_authresponses where response = 'No' group by response_authresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                                cursor.execute("update class_sentence as cs set weight = (weight + 1) from response_authresponses as ar where cs.sentence = ar.sentence AND ar.response='Yes'")
                                connection.commit()
                                return render(request, 'pages/classifier-authority.html', contexta)
                else:
                        return render(request, 'pages/classifier-authority.html', contexta)
        else:
                return render(request, 'pages/classifier-authority.html', contexta)

def classifiersanctity (request):
        responses = request.POST.get('response')
        questionS = Questions.objects.get(id='5')
        random_objects =ClassSentence.objects.raw("SELECT * FROM class_sentence WHERE NOT EXISTS (SELECT * FROM response_sanresponses WHERE class_sentence.sentence = response_sanresponses.sentence) ORDER BY -LOG(1.0 - random()) / weight LIMIT 1")
        user_id = request.user.id
        screen_name = request.user.screen_name
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextS = {
                'random_objects':random_objects,
                'question':questionS,
                'responses':responses,
                'user_id': user_id,
                'screen_name':screen_name,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=SanResponses(question=questionS, sentence=random_objects, response=responses, userid=user_id, screen_name=screen_name, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userid')
                                post.screen_name = request.POST.get('screen_name')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                cursor = connection.cursor()
                                cursor.execute("update response_totals set sanctity_degradation = x.result from (select userid, count(*) as result from response_sanresponses group by response_sanresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set sanctity_degradation_yes = x.result from (select userid, count(*) as result from response_sanresponses where response = 'Yes' group by response_sanresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set sanctity_degradation_no = x.result from (select userid, count(*) as result from response_sanresponses where response = 'No' group by response_sanresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                                cursor.execute("update class_sentence as cs set weight = (weight + 1) from response_sanresponses as sr where cs.sentence = sr.sentence AND sr.response='Yes'")
                                connection.commit()
                                return render(request, 'pages/classifier-sanctity.html', contextS)
                else:
                        return render(request, 'pages/classifier-sanctity.html', contextS)
        else:
                return render(request, 'pages/classifier-sanctity.html', contextS)

def classifierliberty (request):
        responses = request.POST.get('response')
        questionL = Questions.objects.get(id='6')
        random_objects =ClassSentence.objects.raw("SELECT * FROM class_sentence WHERE NOT EXISTS (SELECT * FROM response_libresponses WHERE class_sentence.sentence = response_libresponses.sentence) ORDER BY -LOG(1.0 - random()) / weight LIMIT 1")
        user_id = request.user.id
        screen_name = request.user.screen_name
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextL = {
                'random_objects':random_objects,
                'question':questionL,
                'responses':responses,
                'user_id': user_id,
                'screen_name':screen_name,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=LibResponses(question=questionL, sentence=random_objects, response=responses, userid=user_id, screen_name=screen_name, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userid')
                                post.screen_name = request.POST.get('screen_name')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                cursor = connection.cursor()
                                cursor.execute("update response_totals set liberty_oppression = x.result from (select userid, count(*) as result from response_libresponses group by response_libresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set liberty_oppression_yes = x.result from (select userid, count(*) as result from response_libresponses where response = 'Yes' group by response_libresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set liberty_oppression_no = x.result from (select userid, count(*) as result from response_libresponses where response = 'No' group by response_libresponses.userid) x where x.userid = response_totals.userid")
                                cursor.execute("update response_totals set total = x.result from (select userid, COALESCE(care_harm,0) + COALESCE(fairness_cheating,0) + COALESCE(loyalty_betrayal,0) + COALESCE(authority_subversion,0) + COALESCE(sanctity_degradation,0) + COALESCE(liberty_oppression,0) as result from response_totals) x where x.userid = response_totals.userid;")
                                cursor.execute("update class_sentence as cs set weight = (weight + 1) from response_libresponses as lr where cs.sentence = lr.sentence AND lr.response='Yes'")
                                connection.commit()
                                return render(request, 'pages/classifier-liberty.html', contextL)
                else:
                        return render(request, 'pages/classifier-liberty.html', contextL)
        else:
                return render(request, 'pages/classifier-liberty.html', contextL)

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('splash')
        else:
            messages.error(request, 'User not found')
            return redirect('login')
  
    else: 
        return render(request, 'pages/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')
  
def register(request, *args, **kwargs):
     if request.method == 'POST':
        gender = request.POST['gender']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        email = request.POST['username']
        screen_name = request.POST['screen_name']
        age = request.POST['age']
        country = request.POST['country']
        postal_code =  request.POST['postal_code'] 
        education_attainment =  request.POST['education_attainment'] 
        income =  request.POST['income'] 
        ethnicity =  request.POST['ethnicity'] 
        nationality =  request.POST['nationality'] 
        password = request.POST['password']
        password2 = request.POST['password2']     

       
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Username already used')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already used')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, screen_name=screen_name, username=email, password=password, age=age, country=country, postal_code=postal_code, gender=gender, nationality=nationality, education_attainment=education_attainment, income=income, ethnicity=ethnicity)
                def form_valid(self, form):

                        # get the token submitted in the form
                        recaptcha_response = self.request.POST.get('g-recaptcha-response')
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

                        if (not result['success']) or (not result['action'] == 'signup'):  # make sure action matches the one from your template
                                messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
                                return super().form_invalid(form)
                user.save(*args, **kwargs)
                subject = 'Thank you for registering!'
                message = 'Welcome to the Moral Class App! You have been registered and are ready to start classifying sentences. Thank you from RA2!'
                from_email = settings.EMAIL_HOST_USER
                to_email = [user.email]
                send_mail(subject, message, from_email, to_email, fail_silently=True)

                messages.success(request, 'Your profile has been updated')
                return redirect('tutorial')
     else:
        return render(request, 'pages/register.html', {'site_key': settings.RECAPTCHA_SITE_KEY})

def tutorial (request):
     return render(request, 'pages/tutorial.html')

def tutorial2 (request):
     return render(request, 'pages/tutorial2.html')

def test (request):
        return render(request, 'pages/test.html')

def dashboard (request):
        return render(request, 'pages/dashboard.html')

def dashtutorial (request):
        return render(request, 'pages/dashtutorial.html')

def profile (request):
        args = {'user': request.user}
        return render(request, 'pages/profile.html', args)

def splash (request):
        return render(request, 'pages/splash.html')

def change_password (request):
        if request.method == 'POST':
                form = PasswordChangeForm(data=request.POST, user=request.user)
                if form.is_valid():
                        form.save()
                        update_session_auth_hash(request, form.user)
                        return redirect ('profile')
                else:
                        return redirect('change_password')
               
        else:
                form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'pages/change_password.html', args)

def leaderboard (request):
        totalleads = Totals.objects.values_list('userid', 'total').order_by('-total')[:1]
        careleads = CareResponses.objects.values_list('userid').annotate(id_count=Count('*')).order_by('-id_count')[:5]
        libleads = LibResponses.objects.values_list('userid').annotate(id_count=Count('*')).order_by('-id_count')[:5]
        loyleads = LoyResponses.objects.values_list('userid').annotate(id_count=Count('*')).order_by('-id_count')[:5]
        sanleads = SanResponses.objects.values_list('userid').annotate(id_count=Count('*')).order_by('-id_count')[:5]
        authleads = AuthResponses.objects.values_list('userid').annotate(id_count=Count('*')).order_by('-id_count')[:5]
        fairleads = FairResponses.objects.values_list('userid').annotate(id_count=Count('*')).order_by('-id_count')[:5]
        
        
        args = {'totalleads':totalleads, 'careleads':careleads, 'libleads':libleads, 'loyleads':loyleads, 'sanleads':sanleads, 'authleads':authleads, 'fairleads':fairleads}
        return render(request, 'pages/leaderboard.html', args)

