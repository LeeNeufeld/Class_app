from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from response.models import Responses
from questions.models import Questions
from sentences.models import ClassSentence
from users.models import CustomUser
User = get_user_model()
def index(request):
 return render(request, 'pages/index.html')

def classifier(request):
    responses = request.POST.get('response')
    questions = Questions.objects.order_by('?')[0:1]
    random_objects =ClassSentence.objects.order_by('?')[0:1]
    user_id = request.user.id
    context = {
        'random_objects':random_objects,
        'questions':questions,
        'responses':responses,
        'user_id': user_id
    }
    if request.method =='POST':
        if request.user.is_authenticated:
            if request.POST.get('question') and request.POST.get('random_object') and request.POST.get('response'):
                post=Responses(question=questions, sentence=random_objects, response=responses, userId=user_id)
                post.question=request.POST.get('question')
                post.sentence=request.POST.get('random_object')
                post.response=request.POST.get('response')
                post.userId = request.POST.get('userId')
                post.save()
                return render(request, 'pages/classifier.html', context)
        else:
            return render(request, 'pages/classifier.html', context)
    else:
        return render(request, 'pages/classifier.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('classifier')
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
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password, age=age, country=country, postal_code=postal_code, gender=gender)
                user.save(*args, **kwargs)
                messages.success(request, 'Your profile has been updated')
                return redirect('login')
     else:
        return render(request, 'pages/register.html')
