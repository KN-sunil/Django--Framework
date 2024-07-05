from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

class HelloworldView(View):
    def get(self,request):
     return HttpResponse("<h1>Hello world-cls</h1>")

def getHelloworld(request):
    return HttpResponse("<h1>Hello world-fun</h1>")