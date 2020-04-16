from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse,reverse_lazy
from . import froms, models

# Create your views here.
class SignUp(CreateView):
    form_class = froms.UserCreateForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('login')
