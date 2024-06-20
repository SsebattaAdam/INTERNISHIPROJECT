
from django import urls
from django.urls import path , include
from . import views



urlpatterns = [
  ## These are the landing pages
  path('', views.indexPage, name ='index'),
  path('about/', views.about, name = 'about'),
  path('service/', views.service, name = 'service'),
  path('service_details/', views.service_detail, name = 'service_details'),
  path('get_started/', views.get_startednow, name = 'get_started'),
  
  ## These are the Entreprenuers' urls
  path('entreprenuers/', views.homepage1, name = 'homepage1'),
  path('entreprenuer/ideals/', views.business_ideals, name = 'business_ideals'),
  path("entreprenuer/requests/", views.service_requests, name="service_requests"),
  path("entreprenuer/requests/form", views.service_request_form, name="expert_request_form"),
  path("entreprenuer/schedule/", views.consultation_schedule, name="consultation_schedule"),
  
  ## These are the Investors' urls
  path('investors/', views.investorhomepage, name = 'investorhomepage'),
  
  ## These are the Experts' urls
  path('experts/', views.experthomepage, name = 'experthomepage'),
  path('experts/feedback/', views.feedback, name = 'feedback'),
  ## These are the Registration urls
  path('membership/entreprenuers/', views.register_entreprenuer, name = 'register_entreprenuers'),
  path('membership/investors/', views.register_investor, name='register_investors'),
  path('membership/experts/', views.register_expert, name='register_experts'),
  path('register/',  views.registration_form, name='registration_form'),
  path('register_expert/', views.register_expert, name='register_expert'),
  
  ## This is the Login url
  path('login/',views.login, name ='login'),
  path('logout/', views.logout_view, name='logout'),
  path('loginForm/', views.custom_login, name='custom_login'),

]

