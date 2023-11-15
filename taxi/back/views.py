from django.shortcuts import render
from django.views.generic import ListView
from .models import Driver
# Create your views here.

class DriversList(ListView):
    model = Driver
    template_name = 'drivers.html'
    context_object_name = 'drivers'