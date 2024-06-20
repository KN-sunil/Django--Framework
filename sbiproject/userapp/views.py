from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexpage(request):
    return HttpResponse("INDEX Page")

def servicepage(request):
    return HttpResponse("service page")

def productpage(request):
    return HttpResponse("product page")

def contactpage(request):
    return HttpResponse("contact page")
