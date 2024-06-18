# Bizconnect/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Registration, ExpertRegistration

def indexPage(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')

def service_detail(request):
    return render(request, 'service_details.html')

def get_startednow(request):
    return render(request, 'get_started.html')


def register_entreprenuer(request):
    return render(request, 'entreprenuer/register_entreprenuer.html')
 
def homepage1(request):
    return render(request, 'entreprenuer/homepage1.html')

def register_investor(request):
    return render(request, 'investor/register_investor.html')
def investorhomepage(request):
    return render(request, 'investor/investorHomepage3.html')

def register_expert(request):
    return render(request, 'expert/register_expert.html')
def experthomepage(request):
    return render(request, 'expert/expertHomepage2.html')

def login(request):
    return render(request, 'login.html')
# Create your views here.


from django.shortcuts import render, redirect
from .models import Registration


def registration_form(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        firstname = request.POST.get('firstname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        district = request.POST.get('district')
        country = request.POST.get('country')
        company = request.POST.get('company')
        role_in_company = request.POST.get('role_in_company')
        user_type = "entreprenuer"
        
        # Check if the email is already used
        if Registration.objects.filter(email=email).exists():
            message = 'Email already in use. Please use a different email.'
            return render(request, 'entreprenuer/register_entreprenuer.html', {'message': message})
        
        # Save the data to the Registration model
        Registration.objects.create(
            surname=surname,
            firstname=firstname,
            gender=gender,
            email=email,
            contact=contact,
            district=district,
            country=country,
            company=company,
            role_in_company=role_in_company
        )
        # Redirect to another page after successful submission
        return redirect('homepage1')
    
    return redirect('register_entreprenuers')

def logout_view(request):
    # Redirect to the index page or any other page after logout
    return redirect('index')

def login(request):
    return render(request, 'login.html')




def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('Password')
        

        if Registration.objects.filter(email=email, firstname=password, user_type= "entrepreneur").exists():

            return redirect('homepage1') # Redirect to the homepage after login
        elif ExpertRegistration.objects.filter(email=email, firstname=password, user_type= "expert").exists():
            return redirect('experthomepage') 
        else:
            message = 'Invalid email or password. Please try again.'
            return render(request, 'login.html', {'message': message})

    return render(request, 'login.html')



from django.shortcuts import render, redirect
from .models import ExpertRegistration
import json

def register_expert(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        firstname = request.POST.get('firstname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        district = request.POST.get('district')
        country = request.POST.get('country')
        knowledge = request.POST.getlist('knowledge')
        experience = request.POST.getlist('experience')
        achievements = request.POST.get('achievements')
        references = request.POST.get('references')
        user_type = "expert"
        
        # Check if the email is already used
        if ExpertRegistration.objects.filter(email=email).exists():
            message = 'Email already in use. Please use a different email.'
            return render(request, 'expert/register_expert.html', {'message': message})
        
        # Save the data to the ExpertRegistration model
        expert = ExpertRegistration(
            surname=surname,
            firstname=firstname,
            gender=gender,
            email=email,
            contact=contact,
            district=district,
            country=country,
            experience=experience,
            knowledge=knowledge,
            achievements=achievements,
            references=references,
            user_type=user_type
        )
        expert.save()
        
        # Redirect to another page after successful submission
        return redirect('homepage1')
    
    return render(request, 'expert/register_expert.html')
