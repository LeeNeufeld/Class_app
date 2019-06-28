from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Classifier', views.classifier, name='classifier'),
    path('Login', views.login, name='login'),
    path('Register', views.register, name='register'),
    path('logout', views.logout, name='logout')
  
]