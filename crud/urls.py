from unicodedata import name
from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('leads/create/', views.leads_create, name='leads_create'),
]