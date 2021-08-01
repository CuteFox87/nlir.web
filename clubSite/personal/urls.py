from django.urls import path

from . import views

app_name = 'personal'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('userProfile/editUserInfo/', views.editUserInfo, name='editUserInfo'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('login/authenticateAccount/', views.authenticateAccount, name='authenticateAccount'),
    path('log_out/', views.log_out, name='log_out'),
]