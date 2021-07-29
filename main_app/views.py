from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule

# Create your views here.
def home(request):
    return HttpResponse('Hello world, this is the home route')

