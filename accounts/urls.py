from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordChangeDoneView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.custom_logout, name='logout'),
]
