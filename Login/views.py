from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(TemplateView):
  template_name = "home.html"

class SignUpView(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'sign_up.html'
