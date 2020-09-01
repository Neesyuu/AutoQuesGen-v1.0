from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    date = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    father = forms.CharField()
    mother = forms.CharField()
    plus2name = forms.CharField()
    plus2board = forms.CharField()
    plus2year = forms.CharField()
    plus2percent = forms.CharField()
    slcname = forms.CharField()
    slcboard = forms.CharField()
    slcyear = forms.CharField()
    slcpercent = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date', 'address', 'phone',
                  'father', 'mother',
                  'plus2name', 'plus2board', 'plus2year', 'plus2percent',
                  'slcname', 'slcboard', 'slcyear', 'slcpercent')