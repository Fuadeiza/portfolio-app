from django.contrib.auth import User
from PortfolioApp.models import UserPortfolio, UserProject
from django.db import models
from django import forms



class UserPortfolioForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30) 

    class meta:
        model = UserPortfolio
        exclude =['user']



class UserProjectForm(forms.ModelForm):
    class Meta:
        model = UserProject
        exclude= ['user']