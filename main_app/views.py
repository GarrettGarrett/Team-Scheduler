from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    return render(request, 'home.html')



# Class-based View
class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['name', 
    'SundayStart', 'SundayEnd',
    'MondayStart', 'MondayEnd',
    'TuesdayStart', 'TuesdayEnd',
    'WednesdayStart', 'WednesdayEnd',
    'ThursdayStart', 'ThursdayEnd',
    'FridayStart', 'FridayEnd',
    'SaturdayStart', 'SaturdayEnd',
    ]
    template_name = 'new.html'
    success_url = '/'

class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['name', 
    'SundayStart', 'SundayEnd',
    'MondayStart', 'MondayEnd',
    'TuesdayStart', 'TuesdayEnd',
    'WednesdayStart', 'WednesdayEnd',
    'ThursdayStart', 'ThursdayEnd',
    'FridayStart', 'FridayEnd',
    'SaturdayStart', 'SaturdayEnd',
    ]
    template_name = 'update.html'
    success_url = '/'

class ScheduleDelete(DeleteView):
    model = Schedule
    template_name = 'confirm_delete.html'
    success_url = '/'