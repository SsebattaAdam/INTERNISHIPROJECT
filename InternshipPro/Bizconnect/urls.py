
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
  path("entrepreuner/ideal/form/", views.business_ideal_form , name="business_ideal_form"),
  path("entreprenuer/requests/", views.service_requests, name="service_requests"),
  path("entreprenuer/requests/form/", views.service_request_form, name="expert_request_form"),
  path("entreprenuer/schedule/", views.consultation_schedule, name="consultation_schedule"),
  path("entreprenuer/schedule/form/", views.consultation_schedule_form, name="consultation_schedule_form"),
  path("entreprenuer/investment/deals/", views.investment_deal, name="investment_deals"),
  path("entreprenuer/investment/deals/form/", views.investment_deal_form, name="investment_deal_form"),
  
  ## These are the Investors' urls
  path('investors/', views.investorhomepage, name = 'investorhomepage'),
  path("investor/fundings/", views.investment_fundings, name="investment_fundings"),
  path("investor/funding/form/", views.investment_funding_form, name="investment_funding_form"),
  path('submit-investor/', views.submit_investor_form, name='submit_investor_form'),
  
  ## These are the Experts' urls
  path('experts/', views.experthomepage, name = 'experthomepage'),
  path('expert/library/', views.resources, name = 'resources'),
  path("expert/library/form/", views.resource_form, name="resource_form"),
  path("expert/requests/", views.assistance_request, name="assistance_request"),
  path("expert/consultation/", views.consultation_packages, name="consultation_packages"),
  path("expert/consultation/form/", views.consultation_package_form, name="consultation_package_form"),
  path("expert/feedback/", views.feedback, name="feedback"),
  
  ## These are the Registration urls
  path('membership/entrepreneurs/', views.register_entrepreneur, name = 'register_entrepreneurs'),
  path('membership/investors/', views.register_investor, name='register_investors'),
  path('membership/experts/', views.register_expert, name='register_experts'),
  path('register/',  views.registration_form, name='registration_form'),
  path('register_expert/', views.register_expert, name='register_expert'),
  
  ## This is the Login url
  path('login/',views.login2, name ='login'),
  path('logout/', views.logout_view, name='logout'),
  path('loginForm/', views.custom_login, name='custom_login'),

 
  path('submit_service_request/', views.submit_service_request, name='submit_service_request'),
  path("submit_investment_deal/", views.create_investment_deal, name="create_investment_deal"),


  #admin urls
  path('tables/', views.allTables, name='allTables'),
  # path('list_requestsmade/', views.list_requestsmade, name='list_requestsmade1'),

  path('loginAdmin/', views.loginAdmin, name='loginAdmin'),
  path('logout/', views.logout, name='logout'),
  path('admin2/', views.admin2, name='admin2'),
  path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
  path('create_package/', views.create_consultation_package, name='create_package'),

  path('schedule_meeting/', views.schedule_meeting, name='schedule_meeting'),


  path('update-meeting-status/<int:meeting_id>/<str:status>/', views.update_meeting_status, name='update_meeting_status'),

]
