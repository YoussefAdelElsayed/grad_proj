from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor,Department



class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('fullName', 'photo', 'department','bio',)


class UserNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)




class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('title',)






