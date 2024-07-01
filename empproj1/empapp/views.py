from django.shortcuts import render
from empapp.forms import EmployeeForm,UserForm
from empapp.models import Employee , User
# Create your views here.


def gethomepage(request):
    return render(request,'home.html')

def getempregpage(request):
    empform=EmployeeForm()
    return render(request,'emp.html',{'empform':empform})


# def saveempview(request):

#     if request.method == 'POST':
#        empdata = EmployeeForm(request.POST)       #   here we are saving data based on form class at line 18
#        if(empdata.is_valid()):
#            empdata.save() 
  
#     return render(request,'success.html')

            # another approach

def saveempview(request):
  #   here we are saving data based on model class at line 32
    if request.method == 'POST':
        eid = request.POST.get('eid')
        ename = request.POST.get('ename')
        esal = request.POST.get('esal')
        empdata = Employee(eid=eid,ename=ename,esal=esal)
        empdata.save()                    
 
        # we can write this type also   
        # eid = request.POST['eid']
        # ename = request.POST['ename']
        # esal = request.POST['esal']
     
  
    return render(request,'success.html')

def getnewuserpage(request):
    userform=UserForm()
    return render(request, 'user.html', {'userform':userform})

def saveuserview(request):
    if request.method == 'POST':
      uname=request.POST.get('uname') 
      uloc = request.POST.get('uloc')
      userdata = User(uname=uname,uloc=uloc)
      userdata.save()
    return render(request,'success.html')

