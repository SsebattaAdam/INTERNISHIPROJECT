
from django import urls
from django.urls import path , include
from . import views



urlpatterns = [
     path('', views.indexPage, name ='index'),
     path('about/', views.about, name = 'about')
    
]

