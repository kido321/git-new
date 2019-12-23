from django import forms
from .models import user,Fb
from django.contrib.auth.models import User
class Formname(forms.Form):
    name= forms.CharField()
    username= forms.CharField()
    text=forms.CharField(widget=forms.Textarea)

class Formname1(forms.Form):
    name= forms.CharField()
    username= forms.CharField()
    text=forms.CharField(widget=forms.Textarea)

class Formmodel(forms.ModelForm):
    class Meta():
        model = user
        fields = "__all__"
