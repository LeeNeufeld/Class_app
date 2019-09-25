from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('Classifier', views.classifier, name='classifier'),
    path('Classifier-Fairness', views.classifierfairness,
         name='classifierfairness'),
    path('Classifier-Loyalty', views.classifierloyalty, name='classifierloyalty'),
    path('Classifier-Authority', views.classifierauthority,
         name='classifierauthority'),
    path('Classifier-Sanctity', views.classifiersanctity,
         name='classifiersanctity'),
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
    path('Leaderboard', views.leaderboard, name='leaderboard'),
    path('logout', views.logout, name='logout'),
    path('change-password', views.change_password, name='change_password'),
    path('password-reset', auth_views.PasswordResetView.as_view(
        template_name='pages/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pages/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pages/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/password_reset_complete.html'), name='password_reset_complete'),





]
