# Bizconnect/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Registration, ExpertRegistration
from django.contrib.auth import authenticate, login

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

## Entreprenuers
def register_entreprenuer(request):
    return render(request, 'entreprenuer/register_entreprenuer.html')
 
def homepage1(request):
    return render(request, 'entreprenuer/homepage1.html')

def business_ideals(request):
    return render(request, 'entreprenuer/business_ideals.html')

def service_requests(request):
    return render(request, 'entreprenuer/service_request.html')

def service_request_form(request):
    return render(request, 'entreprenuer/expert_request_form.html')

def consultation_schedule(request):
    return render(request, 'entreprenuer/consultation_schedule.html')

def consultation_schedule_form(request):
    return render(request, 'entreprenuer/consultation_schedule_form.html')

def investment_deals(request):
    return render(request, 'entreprenuer/investment_deals.html')

def investment_deal_form(request):
    return render(request, 'entreprenuer/investment_deal_form.html')

## Investors
def register_investor(request):
    return render(request, 'investor/register_investor.html')
def investorhomepage(request):
    return render(request, 'investor/investorHomepage3.html')

## Experts
def register_expert(request):
    return render(request, 'expert/register_expert.html')
def experthomepage(request):
    return render(request, 'expert/expertHomepage2.html')
def resources(request):
    return render(request, 'expert/resources.html')
def resource_form(request):
    return render(request, 'expert/resource_form.html')
def assistance_request(request):
    return render(request, 'expert/assistance_request.html')
def consultation_packages(request):
    return render(request, 'expert/consultation_packages.html')
def consultation_package_form(request):
    return render(request, 'expert/consultation_package_form.html')
def feedback(request):
    return render(request, 'expert/feedback.html')

def login(request):
    return render(request, 'login.html')


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


from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import ServiceRequest

def submit_service_request(request):
    if request.method == 'POST':
        business_idea = request.POST.get('title')
        industry = request.POST.get('industry')
        description = request.POST.get('description')
        target_market = request.POST.get('market')
        consultation_time = request.POST.get('consultation_time')
        consultation_date = request.POST.get('consultation_date')
        urgency_level = request.POST.get('urgency_level')
        comments = request.POST.get('comments')
        attachment = request.FILES.get('attachment')

        if attachment:
            fs = FileSystemStorage(location='attachments/')
            attachment_file = fs.save(attachment.name, attachment)
            attachment_url = fs.url(attachment_file)
        else:
            attachment_url = None

        ServiceRequest.objects.create(
            business_idea=business_idea,
            industry=industry,
            description=description,
            target_market=target_market,
            consultation_time=consultation_time,
            consultation_date=consultation_date,
            urgency_level=urgency_level,
            attachment=attachment_url,
            comments=comments,
        )

        return redirect('homepage1')  # Redirect to a success page or another page after submission

    return render(request, 'service_request_form.html')

# admin views
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password )
        if user is not None:
            login(request, user)
            return redirect('admin2')
        else:
            return render(request, 'login2.html', {'error': 'Invalid credentials'})
    return render(request, 'login2.html')

def allTables(request):
    return render(request, 'pages/tables/simple.html')

def logout(request):
    return render(request, 'login2.html')

def loginAdmin(request):
    return render(request, 'login2.html')

def admin2(request):
    return render(request, 'index2.html')

#end of admin views