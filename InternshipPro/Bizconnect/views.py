# Bizconnect/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse



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

# Create your views here.
