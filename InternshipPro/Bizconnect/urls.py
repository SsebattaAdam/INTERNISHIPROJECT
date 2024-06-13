
from django import urls
from django.urls import path , include
from . import views



urlpatterns = [
     path('', views.indexPage, name ='index'),
     path('about/', views.about, name = 'about'),
     path('service/', views.service, name = 'service'),
     path('service_details/', views.service_detail, name = 'service_details'),
     path('get_started/', views.get_startednow, name = 'get_started'),
     path('membership/entreprenuers/', views.register_entreprenuer, name = 'register_entreprenuers'),
     path('membership/investors/', views.register_investor, name='register_investors'),
     path('membership/experts/', views.register_expert, name='register_experts'),
    
]

