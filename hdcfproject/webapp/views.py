from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getindex(request):
    return HttpResponse("index page")

def getabout(request):
    return HttpResponse("About page")

def getservice(request):
    return HttpResponse("Service page")

def getcontact(request):
    return HttpResponse("Contact page")

