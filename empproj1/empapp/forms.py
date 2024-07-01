from django import forms
from empapp.models import Employee,User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['eid','ename','esal']
        # fields="__all__",

class UserForm(forms.Form):
    uname = forms.CharField(max_length=32, label="User Name")
    uloc = forms.CharField(max_length=32,label="Location")