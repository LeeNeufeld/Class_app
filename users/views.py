from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.core.mail import send_mail
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from response.models import Responses
from questions.models import Questions
from sentences.models import ClassSentence
from users.models import CustomUser

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
    random_objects =ClassSentence.objects.order_by('?')[0:1]
    user_id = request.user.id
    age = request.user.age
    gender = request.user.gender
    postal_code = request.user.postal_code
    country = request.user.country
    context = {
        'random_objects':random_objects,
        'question':question,
        'responses':responses,
        'user_id': user_id,
        'age': age,
        'gender': gender,
        'postal_code': postal_code,
        'country': country

    }
    if request.method =='POST':
        if request.user.is_authenticated:
            if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                post=Responses(question=question, sentence=random_objects, response=responses, userId=user_id, age=age, gender=gender, postal_code=postal_code, country=country)
                post.question=request.POST.get('question')
                post.sentence=request.POST.get('random_object')
                post.response=request.POST.get('response')
                post.userId = request.POST.get('userId')
                post.age = request.POST.get('age')
                post.gender = request.POST.get('gender')
                post.postal_code = request.POST.get('postal_code')
                post.country = request.POST.get('country')
                post.save()
                return render(request, 'pages/classifier.html', context)
        else:
            return render(request, 'pages/classifier.html', context)
    else:
        return render(request, 'pages/classifier.html', context)


def classifierfairness (request):
        responses = request.POST.get('response')
        questionf = Questions.objects.get(id='2')
        random_objects =ClassSentence.objects.order_by('?')[0:1]
        user_id = request.user.id
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextf = {
                'random_objects':random_objects,
                'question':questionf,
                'responses':responses,
                'user_id': user_id,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=Responses(question=questionf, sentence=random_objects, response=responses, userId=user_id, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userId')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                return render(request, 'pages/classifier-fairness.html', contextf)
                else:
                        return render(request, 'pages/classifier-fairness.html', contextf)
        else:
                return render(request, 'pages/classifier-fairness.html', contextf)

def classifierloyalty (request):
        responses = request.POST.get('response')
        questionl = Questions.objects.get(id='3')
        random_objects =ClassSentence.objects.order_by('?')[0:1]
        user_id = request.user.id
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextl = {
                'random_objects':random_objects,
                'question':questionl,
                'responses':responses,
                'user_id': user_id,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=Responses(question=questionl, sentence=random_objects, response=responses, userId=user_id, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userId')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                return render(request, 'pages/classifier-loyalty.html', contextl)
                else:
                        return render(request, 'pages/classifier-loyalty.html', contextl)
        else:
                return render(request, 'pages/classifier-loyalty.html', contextl)

def classifierauthority (request):
        responses = request.POST.get('response')
        questiona = Questions.objects.get(id='4')
        random_objects =ClassSentence.objects.order_by('?')[0:1]
        user_id = request.user.id
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contexta = {
                'random_objects':random_objects,
                'question':questiona,
                'responses':responses,
                'user_id': user_id,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=Responses(question=questiona, sentence=random_objects, response=responses, userId=user_id, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userId')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                return render(request, 'pages/classifier-authority.html', contexta)
                else:
                        return render(request, 'pages/classifier-authority.html', contexta)
        else:
                return render(request, 'pages/classifier-authority.html', contexta)

def classifiersanctity (request):
        responses = request.POST.get('response')
        questionS = Questions.objects.get(id='5')
        random_objects =ClassSentence.objects.order_by('?')[0:1]
        user_id = request.user.id
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextS = {
                'random_objects':random_objects,
                'question':questionS,
                'responses':responses,
                'user_id': user_id,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=Responses(question=questionS, sentence=random_objects, response=responses, userId=user_id, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userId')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
                                return render(request, 'pages/classifier-sanctity.html', contextS)
                else:
                        return render(request, 'pages/classifier-sanctity.html', contextS)
        else:
                return render(request, 'pages/classifier-sanctity.html', contextS)

def classifierliberty (request):
        responses = request.POST.get('response')
        questionL = Questions.objects.get(id='6')
        random_objects =ClassSentence.objects.order_by('?')[0:1]
        user_id = request.user.id
        age = request.user.age
        gender = request.user.gender
        postal_code = request.user.postal_code
        country = request.user.country
        contextL = {
                'random_objects':random_objects,
                'question':questionL,
                'responses':responses,
                'user_id': user_id,
                'age': age,
                'gender': gender,
                'postal_code': postal_code,
                'country':country
        }
        if request.method =='POST':
                if request.user.is_authenticated:
                        if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                                post=Responses(question=questionL, sentence=random_objects, response=responses, userId=user_id, age=age, gender=gender, postal_code=postal_code, country=country)
                                post.question=request.POST.get('question')
                                post.sentence=request.POST.get('random_object')
                                post.response=request.POST.get('response')
                                post.userId = request.POST.get('userId')
                                post.age = request.POST.get('age')
                                post.gender = request.POST.get('gender')
                                post.postal_code = request.POST.get('postal_code')
                                post.country = request.POST.get('country')
                                post.save()
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
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password, age=age, country=country, postal_code=postal_code, gender=gender, nationality=nationality, education_attainment=education_attainment, income=income, ethnicity=ethnicity)
                user.save(*args, **kwargs)
                subject = 'Thank you for registering!'
                message = 'Welcome to the Moral Class App! You have been registered and are ready to start classifying sentences. Thank you from RA2!'
                from_email = settings.EMAIL_HOST_USER
                to_email = [user.email]
                send_mail(subject, message, from_email, to_email, fail_silently=True)

                messages.success(request, 'Your profile has been updated')
                return redirect('tutorial')
     else:
        return render(request, 'pages/register.html')

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