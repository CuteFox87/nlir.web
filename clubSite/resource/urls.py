from django.urls import path

from . import views

app_name = 'resource'

urlpatterns = [
    path('problem/updateResult', views.updateResult, name='updateResult'),
    path('problem/', views.problem, name='problem'),
]