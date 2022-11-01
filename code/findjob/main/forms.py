from django import forms
from django.core.exceptions import ValidationError

from main.models import Dreamreal


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get("username")
        dbuser = Dreamreal.objects.filter(name=username)

        if not dbuser:
            return "db doesn't has %s" % username
        return username


class DreamrealForm(forms.Form):
    lastname = forms.CharField(max_length=50)
    firstname = forms.CharField(max_length=50)
    pid = forms.CharField(max_length=50, unique=True)
    email = forms.CharField(max_length=50, unique=True)
    passwd = forms.CharField(max_length=50)


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()
