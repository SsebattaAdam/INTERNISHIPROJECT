# InternishipApp/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def functionCall(request):
    return HttpResponse("Hello world")

def indexPage(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
# Create your views here.
