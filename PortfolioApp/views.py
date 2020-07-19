from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import UserPortfolio, UserProject
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView
from django.contrib.auth.models import User
from django.db import models
# Create your views here.

app_name='PortfolioApp'


class index(TemplateView):
    template_name = "PortfolioApp/index.html"


class UserPortfolioUpdateView(LoginRequiredMixin, UpdateView):
    #permission needed here
    model = UserPortfolio
    fields= ['linkedin_username','phone_number', 'github_username','twitter_username','facebook_username','profile_pic']
    template_name = "PortfolioApp/userportfolio.html"

    def get_object(self):
        try:
            userportfolio = UserPortfolio.objects.get(pk=self.request.GET.get('pk'))
        except UserPortfolio.DoesNotExist:
            user = None
        


class UserListView(LoginRequiredMixin, ListView):
    model= UserPortfolio
    template_name= 'PortfolioApp/userlist.html'
    context_object_name='user_list'


class UserDetailView(LoginRequiredMixin, DetailView): 
    # specify the model to use 
    model = UserPortfolio
    context_object_name='user_detail'
    slug_field = 'id'
    template_name='PortfolioApp/userdetail.html'


