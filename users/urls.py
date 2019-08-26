from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Classifier', views.classifier, name='classifier'),
    path('Classifier-Fairness', views.classifierfairness, name='classifierfairness'),
    path('Classifier-Loyalty', views.classifierloyalty, name='classifierloyalty'),
    path('Classifier-Authority', views.classifierauthority, name='classifierauthority'),
    path('Classifier-Sanctity', views.classifiersanctity, name='classifiersanctity'),
    path('Classifier-Liberty', views.classifierliberty, name='classifierliberty'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('Login', views.login, name='login'),
    path('Splash', views.splash, name='splash'),
    path('Register', views.register, name='register'),
    path('Profile', views.profile, name='profile'),
    path('EditProfile', views.editprofile, name='editprofile'),
    path('Tutorial', views.tutorial, name='tutorial'),
    path('DashTutorial', views.dashtutorial, name='dashtutorial'),
    path('Tutorial2', views.tutorial2, name='tutorial2'),
    path('Test', views.test, name='test'),
    path('logout', views.logout, name='logout'),
 
  
]