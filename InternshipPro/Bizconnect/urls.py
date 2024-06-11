
from django import urls
from django.urls import path , include
from . import views



urlpatterns = [
     path('', views.indexPage, name ='index'),
     path('about/', views.about, name = 'about'),
     path('service/', views.service, name = 'service'),
     path('service_details/', views.service_detail, name = 'service_details'),
     path('get_started/', views.get_startednow, name = 'get_started'),
    
]

