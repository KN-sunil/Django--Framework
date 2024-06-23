from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def getindexpage(request):
    eid=101
    ename='SUNIL KN'
    return render(request,'index.html',context={'eid':eid,'ename':ename})

def getcontactpage(request):
    mydata={'currenttime':datetime.datetime.now()}
    return render(request,'contact.html',context=mydata)