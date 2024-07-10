# Bizconnect/views.py
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from .decorators import is_entrepreneur, is_expert, is_investor, login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Registration, ExpertRegistration, InvestmentDeal
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .models import BusinessIdeas


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

def after_register(request):
    return render(request, 'after_register.html')

## entrepreneurs
def register_entrepreneur(request):
    return render(request, 'entrepreneur/register_entrepreneur.html')
 
@login_required
def homepage1(request):
    return render(request, 'entrepreneur/homepage1.html')

@login_required
def business_ideals(request):
    if request.session['user_type'] == "entrepreneur":
        entrepreneur = get_object_or_404(Registration, id=request.session['user_id'])
        ideals = BusinessIdeas.objects.filter(entrepreneur=entrepreneur)
    else:
        ideals = BusinessIdeas.objects.all()
    return render(request, 'entrepreneur/business_ideals.html', {'proposals': ideals,})

@login_required
@is_entrepreneur
def business_ideal_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        industry = request.POST.get('industry')
        target_market = request.POST.get('market')
        business_model = request.POST.get('business-model')
        projections = request.POST.get('projections')
        goals = request.POST.get('goals')
        
        pitch_deck = request.FILES.get('pitch-deck')
        plan = request.FILES.get('plan')
        video = request.FILES.get('video')
        support = request.FILES.get('support')
        entrepreneur = get_object_or_404(Registration, id=request.session['user_id'])

        business_idea = BusinessIdeas(
            title=title,
            description=description,
            industry=industry,
            target_market=target_market,
            business_model=business_model,
            projections=projections,
            goals=goals,
            pitch_deck=pitch_deck,
            plan=plan,
            video=video,
            support=support,
            entrepreneur=entrepreneur,
        )
        
        business_idea.save()
        return redirect('business_ideals')
    
    return render(request, 'entrepreneur/business_ideal_form.html')

@login_required
def service_requests(request):
    if request.session['user_type'] == "entrepreneur":
        entrepreneur = get_object_or_404(Registration, id=request.session['user_id'])
        completed_requests = ServiceRequest.objects.filter(requester=entrepreneur, status="Completed")
    else:
        completed_requests = ServiceRequest.objects.filter(status='Completed')
    return render(request, 'entrepreneur/service_request.html', {
        'completed_requests': completed_requests,
    })

@login_required
def service_request_form(request):
    return render(request, 'entrepreneur/expert_request_form.html')

@login_required
def consultation_schedule(request):
    user_id = request.session.get('user_id')
    approved_meetings = ScheduledMeeting.objects.filter(status='Approved', entrepreneur = user_id)
    context = {'approved_meetings': approved_meetings,}
    return render(request, 'entrepreneur/consultation_schedule.html', context)

@login_required
def investment_deals(request):
    investment_deals = InvestmentDeal.objects.all()
    return render(request, 'entrepreneur/investment_deals.html', {'deals': investment_deals,})

@login_required
def investment_deal_form(request):
    return render(request, 'entrepreneur/investment_deal_form.html')

## Investors
def register_investor(request):
    return render(request, 'investor/register_investor.html')

@login_required
def investorhomepage(request):
    return render(request, 'investor/investorHomepage3.html')

@login_required
def investment_fundings(request):
    return render(request, 'investor/investment_fundings.html')

@login_required
def investment_funding_form(request):
    return render(request, 'investor/investment_funding_form.html')

@login_required
def investor_deals(request):
    return render(request, 'investor/investor_deals.html')

@login_required
def businessidea_detail(request, idea_id):
    idea = get_object_or_404(businessidea_detail, id=idea_id)
    return render(request, 'businessidea_detail.html', {'idea': idea})
## Experts
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
        )
        expert.save()
        
        return redirect('after_register')
    
    return render(request, 'expert/register_expert.html')

@login_required
def experthomepage(request):
    return render(request, 'expert/expertHomepage2.html')

@login_required
def resources(request):
    return render(request, 'expert/resources.html')

@login_required
def resource_form(request):
    return render(request, 'expert/resource_form.html')

@login_required
@is_expert
def assistance_request(request):
    expert = get_object_or_404(ExpertRegistration, pk=request.session['user_id'])
    requests = ServiceRequest.objects.filter(assigned_expert=expert, status='Completed')
    return render(request, 'expert/assistance_request.html', {'requests': requests})

@login_required
@is_expert
def consultation_packages(request):
    expert = get_object_or_404(ExpertRegistration, pk=request.session['user_id'])
    packages = ConsultationPackage.objects.filter(expert=expert)
    return render(request, 'expert/consultation_packages.html', {"packages": packages})

@login_required
def consultation_package_form(request):
    return render(request, 'expert/consultation_package_form.html')

@login_required
def feedback(request):
    return render(request, 'expert/feedback.html')

@login_required
def feedback(request):
    return render(request, 'expert/feedback.html')

def login2(request):
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
        
        # Check if the email is already used
        if Registration.objects.filter(email=email).exists():
            message = 'Email already in use. Please use a different email.'
            return render(request, 'entrepreneur/register_entrepreneur.html', {'message': message})
        
        # Save the data to the Registration model
        entrepreneur = Registration.objects.create(
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
        entrepreneur.save()
        return redirect('after_register')
    
    return redirect('register_entrepreneurs')


def logout_view(request):
    try:
        del request.session["user_id"]
        del request.session["user_type"]
    except KeyError:
        pass    
    return redirect('index')


def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('Password')
        

        if Registration.objects.filter(email=email, firstname=password, user_type= "entrepreneur").exists():
            ent = Registration.objects.get(email=email)
            request.session['user_id'] = ent.id
            request.session['user_type'] = ent.user_type
            return redirect('homepage1') # Redirect to the homepage after login
        elif ExpertRegistration.objects.filter(email=email, firstname=password, user_type= "expert").exists():
            expert = ExpertRegistration.objects.get(email=email)
            request.session["user_id"] = expert.id
            request.session['user_type'] = expert.user_type
            return redirect('experthomepage') 
        elif Investor.objects.filter(email=email, country=password, user_type = "investor").exists():
            investor = Investor.objects.get(email=email)
            request.session['user_id'] = investor.id
            return redirect('investorhomepage')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid email or password. Please try again.')
            return render(request, 'login.html')

    return render(request, 'login.html')


@login_required
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
        entrepreneur = get_object_or_404(Registration, id=request.session['user_id'])

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
            requester=entrepreneur
        )

        return redirect('homepage1')  # Redirect to a success page or another page after submission

    return render(request, 'service_request_form.html')
#posting business ideas
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import BusinessIdeas


# admin views

@login_required
def logout2(request):
    return render(request, 'login2.html')

def loginAdmin(request):
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

def admin2(request):
    return render(request, 'index2.html')

@login_required
def allTables(request):
    requests = ServiceRequest.objects.all()
    scheduled_meetings = ScheduledMeeting.objects.all()
    reply_requests = ReplyRequest.objects.all()
    context = {
        'requests': requests,
        'scheduled_meetings': scheduled_meetings,
        'reply_requests': reply_requests
    }
    return render(request, 'pages/tables/simple.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest



@login_required
def approve_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        expert_id = request.POST.get('expert')
        if expert_id:
            expert = get_object_or_404(ExpertRegistration, id=expert_id)
            service_request.assigned_expert = expert
        service_request.status = 'Completed'
        service_request.save()
        return redirect('allTables')
    experts = ExpertRegistration.objects.filter(user_type='expert')
    return render(request, 'pages/tables/approve_request.html', {'request': service_request, 'experts': experts})


#end of admin views

@login_required
def list_requestsmade(request):
    pending_requests = ServiceRequest.objects.filter(status='Pending')
    completed_requests = ServiceRequest.objects.filter(status='Completed')
    denied_meetings = ScheduledMeeting.objects.filter(status='Denied')
    approved_meetings = ScheduledMeeting.objects.filter(status='Approved')
    context = {
        'pending_requests': pending_requests,
        'completed_requests': completed_requests,
        'denied_meetings': denied_meetings,
        'approved_meetings': approved_meetings
    }
    return render(request, 'entrepreneur/tables4ent.html', context)




def create_investment_deal(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        industry = request.POST.get('industry')
        funding_goal = request.POST.get('funding-goal')
        valuation = request.POST.get('valuation')
        terms = request.POST.get('terms')

      
        entrepreneur = get_object_or_404(Registration, id=request.session.get('user_id'))

            # Create the investment deal with the fetched entrepreneur
        investment_deal = InvestmentDeal(
                title=title,
                industry=industry,
                funding_goal=funding_goal,
                valuation=valuation,
                terms=terms,
                entrepreneur_id=entrepreneur.id  # Assigning the ID directly
            )
        investment_deal.save()
        return redirect('homepage1')

    return redirect('investment_deals')


#consultation packages
from .models import ConsultationPackage, ScheduledMeeting

@login_required
def create_consultation_package(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        package_type = request.POST.get('industry')
        package_price = request.POST.get('package-price')

        expert = get_object_or_404(ExpertRegistration, pk=request.session['user_id']) # Assuming the logged-in user is the expert

        package = ConsultationPackage.objects.create(
            title=title,
            description=description,
            package_type=package_type,
            package_price=package_price,
            expert=expert
        )
        package.save()

        return redirect('experthomepage')  # Redirect to expert homepage or another URL
    
    return render(request, 'consultation_package_form')

@login_required
def consultation_schedule_form(request, request_id):
    completed_request = get_object_or_404(ServiceRequest, pk=request_id, status='Completed')
    consultation_packages = ConsultationPackage.objects.all()
    context = {
        'consultation_packages': consultation_packages,
        'completed_request': completed_request
    }
    return render(request, 'entrepreneur/consultation_schedule_form.html', context )

@login_required
def schedule_meeting4theent(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        expert_name = request.POST.get('expert')
        consultation_date = request.POST.get('consultation_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        link = request.POST.get('link')
        package_id = request.POST.get('consultation_package')
        entrepreneur = get_object_or_404(Registration, id=request.session.get('user_id'))

        consultation_package = ConsultationPackage.objects.get(pk=package_id)

        # Save your meeting scheduling logic here, 
        schedule_meeting = ScheduledMeeting.objects.create(
            title=title,
            expert_name=expert_name,
            consultation_date=consultation_date,
            start_time=start_time,
            end_time=end_time,
            link=link,
            consultation_package=consultation_package,
            entrepreneur= entrepreneur 
        )
        schedule_meeting.save()
       
        return redirect('homepage1')  
    consultation_packages = ConsultationPackage.objects.all()
    context = {
        'consultation_packages': consultation_packages
    }
    return redirect('consultation_schedule_form', context)


from django.views.decorators.http import require_POST

@login_required
@require_POST
def update_meeting_status(request, meeting_id, status):
    meeting = get_object_or_404(ScheduledMeeting, id=meeting_id)
    
    if status == 'Denied':
        denial_reason = request.POST.get('denial_reason', '')
        meeting.status = 'Denied'
        meeting.denial_reason = denial_reason
    elif status == 'Approved':
        meeting.status = 'Approved'
    elif status == 'Pending':
        meeting.status = 'Pending'
    
    meeting.save()
    return redirect('allTables')


from django.shortcuts import render, redirect
from .models import Investor

def submit_investor_form(request):
    if request.method == 'POST':
        form_type = request.POST.get('type')

        # Common fields
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        country = request.POST.get('country')
        capital = request.POST.get('capital')
        information = request.POST.get('information')
        
        # Preferences
        preferences = {
            'tourism': request.POST.get('tourism', False)== 'tourism',
            'media': request.POST.get('media', False) == 'media',
            'commercial': request.POST.get('commercial', False) == 'commercial',
            'estate': request.POST.get('estate', False) == 'estate',
            'manufacturing': request.POST.get('manufacturing', False) == 'manufacturing',
            'education': request.POST.get('education', False) == 'education',
            'health': request.POST.get('health', False) == 'health',
            'wholesale': request.POST.get('wholesale', False) == 'wholesale',
        }
        # Check if the email is already used
        if Investor.objects.filter(email=email).exists():
            message = 'Email already in use. Please use a different email.'
            return redirect('register_investors', {'message': message})

        if form_type == 'individual':
            # Individual-specific fields
            surname = request.POST.get('surname')
            firstname = request.POST.get('firstname')
            gender = request.POST.get('gender')
            
            investor = Investor.objects.create(
                type='individual',
                email=email,
                contact=contact,
                country=country,
                capital=capital,
                information=information,
                surname=surname,
                firstname=firstname,
                gender=gender,
                **preferences
            )

        elif form_type == 'organization':
            # Organization-specific fields
            company = request.POST.get('company')

            investor = Investor.objects.create(
                type='organization',
                email=email,
                contact=contact,
                country=country,
                capital=capital,
                information=information,
                company=company,
                **preferences
            )
        investor.save()

        return redirect('after_register') 
    return redirect('register_investors') 

def investment_deallists(request):
    investment_deals = InvestmentDeal.objects.all()

    # Handling search query
    query = request.GET.get('q')
    if query:
        investment_deals = investment_deals.filter(
            title__icontains=query) | investment_deals.filter(
            industry__icontains=query)  # Adjust as per your fields

    context = {
        'deals': investment_deals,
    }
    return render(request, 'investor/investor_deals.html', context)



def replay_requests_made(request):
    approved_meetings = ScheduledMeeting.objects.filter(status='Approved')
    context = {
        'approved_meetings': approved_meetings
    }
    return render(request, 'expert/reply.html', context)


from .models import ReplyRequest

def replay_requests_madetothemeeting(request):
    if request.method == 'POST':
        meeting_id = request.POST.get('meeting_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        text_area = request.POST.get('text_area')

        # Assuming ScheduledMeeting and other necessary imports are present
        meeting = ScheduledMeeting.objects.get(pk=meeting_id)

        reply_request = ReplyRequest.objects.create(
            meeting=meeting,
            title=title,
            description=description,
            text_area=text_area,
            status='NOT_SENT'  # Set default status
        )
        reply_request.save()

 
        return redirect('investorhomepage')  
    return render(request, 'expert/reply.html')

def forward_request(request, request_id):
    request_instance = get_object_or_404(ReplyRequest, id=request_id)

    # Update status to 'SENT' (pseudo code, replace with actual logic)
    request_instance.status = 'SENT'
    request_instance.save()

    # Prepare context with specific fields to forward
    context = {
        'title': request_instance.title,
        'description': request_instance.description,
        'text_area': request_instance.text_area,
    }

    return render(request, 'forwarded_table.html', context)