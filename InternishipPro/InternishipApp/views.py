# InternishipApp/views.py
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
# Create your views here.
