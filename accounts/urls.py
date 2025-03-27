from django.contrib import admin
from django.urls import path 
from .views import CustomPasswordChangeView, edit_profile, custom_logout, register , user_login  
from django.contrib.auth.views import PasswordChangeDoneView


urlpatterns = [
    path("register/", register , name="register"),
    path("login/", user_login , name="login"),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('logout/', custom_logout, name='logout'),
]
