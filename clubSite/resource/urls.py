from django.urls import path

from . import views

app_name = 'resource'

urlpatterns = [
    path('problem/', views.problem, name='problem'),
]