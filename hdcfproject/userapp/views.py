from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def wish(request):
    return HttpResponse("WELCOME TO DJANGO")


def index(request):
    return HttpResponse("INDEX PAGE")


def about(request):
    return HttpResponse("ABOUT PAGE")


def service(request):
    return HttpResponse("SERVICE PAGE")
