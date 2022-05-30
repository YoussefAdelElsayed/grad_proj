from django import forms
from .models import Home,Degree


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ("slide","slide2","slide3","about","Awarded"
                    ,"Awarded2","coun","coun2","coun3","coun4",)


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ("Qualifi", "Celsius",)
