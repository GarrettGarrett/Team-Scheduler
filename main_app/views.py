from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Schedule

# schedules = Schedule.objects.all()

def home(request):
    def get_availability(): # Calculating available times:
        schedules = Schedule.objects.all()
        total_users = len(schedules)
        sundayArray = []
        mondayArray = []
        tuesdayArray = []
        wednesdayArray = []
        thursdayArray = []
        fridayArray = []
        saturdayArray = []
        for schedule in schedules:
            # Sunday
            sunday_list = list(range(schedule.SundayStart, schedule.SundayEnd))
            for i in sunday_list:
                sundayArray.append(int(i) + .5)

            # Monday
            monday_list = list(range(schedule.MondayStart, schedule.MondayEnd))
            for i in monday_list:           
                mondayArray.append(int(i) + .5)

            # Tuesday
            tuesday_list = list(range(schedule.TuesdayStart, schedule.TuesdayEnd))
            for i in tuesday_list:           
                tuesdayArray.append(int(i) + .5)

            # Wednesday
            wednesday_list = list(range(schedule.WednesdayStart, schedule.WednesdayEnd))
            for i in wednesday_list:           
                wednesdayArray.append(int(i) + .5)

            # Thursday
            thursday_list = list(range(schedule.ThursdayStart, schedule.ThursdayEnd))
            for i in thursday_list:           
                thursdayArray.append(int(i) + .5)

            # Friday
            friday_list = list(range(schedule.FridayStart, schedule.FridayEnd))
            for i in friday_list:           
                fridayArray.append(int(i) + .5)

            # Saturday
            saturday_list = list(range(schedule.SaturdayStart, schedule.SaturdayEnd))
            for i in saturday_list:           
                saturdayArray.append(int(i) + .5)


        def find_availability(array, total_users):
            availability_array = []
            availability_window_array = []
            for i in array:
                if int(total_users) == int(array.count(i)):
                    availability_array.append(i)

            if len(availability_array) > 0:
                unique_array  = []
                for i in availability_array:
                    if i not in unique_array:
                        unique_array.append(i)
                    
                for i in unique_array:
                    one_hour_window = []
                    if i == .5: # Unavailable
                        # one_hour_window.append(int(0))
                        # one_hour_window.append(int(0))
                        pass
                    if i == 12.5: # 12 PM
                        one_hour_window.append(int(i - .5))
                        one_hour_window.append(int(1))
                    if i == 13.5: # 1 PM
                        one_hour_window.append(int(1))
                        one_hour_window.append(int(2))
                    if i == 14.5: # 2 PM
                        one_hour_window.append(int(2))
                        one_hour_window.append(int(3))
                    if i == 15.5: # 3 PM
                        one_hour_window.append(int(3))
                        one_hour_window.append(int(4))
                    if i == 16.5: # 4 PM
                        one_hour_window.append(int(4))
                        one_hour_window.append(int(5))
                    if i == 17.5: # 5 PM
                        one_hour_window.append(int(5))
                        one_hour_window.append(int(6))
                    if i == 18.5: # 6 PM
                        one_hour_window.append(int(6))
                        one_hour_window.append(int(7))
                    if i == 19.5: # 7 PM
                        one_hour_window.append(int(7))
                        one_hour_window.append(int(8))
                    if i == 20.5: # 8 PM
                        one_hour_window.append(int(8))
                        one_hour_window.append(int(9))
                    if i == 21.5: # 9 PM
                        one_hour_window.append(int(9))
                        one_hour_window.append(int(10))
                    if i == 22.5: # 10 PM
                        one_hour_window.append(int(10))
                        one_hour_window.append(int(11))
                    if i == 22.5: # 11 PM
                        one_hour_window.append(int(11))
                        one_hour_window.append(int(12))
                    else:
                        pass   
                    availability_window_array.append(one_hour_window)

            final_availability_window_array = [] #handles error time input
            for i in availability_window_array:
                if len(i) > 0:
                    final_availability_window_array.append(i)
            return final_availability_window_array

        
        sunday_availability = find_availability(sundayArray, total_users)
        monday_availability = find_availability(mondayArray, total_users)
        tuesday_availability = find_availability(tuesdayArray, total_users)
        wednesday_availability = find_availability(wednesdayArray, total_users)
        thursday_availability = find_availability(thursdayArray, total_users)
        friday_availability = find_availability(fridayArray, total_users)
        saturday_availability = find_availability(saturdayArray, total_users)

            
        return sunday_availability, monday_availability, tuesday_availability, wednesday_availability, thursday_availability, friday_availability, saturday_availability

    # Availability by Day
    schedules = Schedule.objects.all()
    total_users = len(schedules)
    sunday_availability, monday_availability, tuesday_availability, wednesday_availability, thursday_availability, friday_availability, saturday_availability = get_availability()  
    
    # Total Number of Available Time Slots by Day
    total_openings = len(sunday_availability) + len(monday_availability) + len(tuesday_availability) + len(wednesday_availability) + len(thursday_availability) + len(friday_availability) + len(saturday_availability)

    # Total Hours of Availability by User
    def get_total_hours_available():
        schedules = Schedule.objects.all()
        availability_by_user_array = []
        for schedule in schedules:
            total_hours = 0
            # Sunday
            if schedule.SundayEnd >= schedule.SundayStart:
                total_hours += (schedule.SundayEnd - schedule.SundayStart)
            # Monday
            if schedule.MondayEnd >= schedule.MondayStart:
                total_hours += (schedule.MondayEnd - schedule.MondayStart)
            # Tuesday
            if schedule.TuesdayEnd >= schedule.TuesdayStart:
                total_hours += (schedule.TuesdayEnd - schedule.TuesdayStart)
            # Wednesday
            if schedule.WednesdayEnd >= schedule.WednesdayStart:
                total_hours += (schedule.WednesdayEnd - schedule.WednesdayStart)
            # Thursday
            if schedule.ThursdayEnd >= schedule.ThursdayStart:
                total_hours += (schedule.ThursdayEnd - schedule.ThursdayStart)
            # Friday
            if schedule.FridayEnd >= schedule.FridayStart:
                total_hours += (schedule.FridayEnd - schedule.FridayStart)
            # Saturday
            if schedule.SaturdayEnd >= schedule.SaturdayStart:
                total_hours += (schedule.SaturdayEnd - schedule.SaturdayStart)
            
            availability_by_user_array.append(total_hours)
        return availability_by_user_array
            
    
    total_hours_by_user = get_total_hours_available()

    def getTime(schedule):
        total_hours = 0
        # Sunday
        if schedule.SundayEnd >= schedule.SundayStart:
            total_hours += (schedule.SundayEnd - schedule.SundayStart)
        # Monday
        if schedule.MondayEnd >= schedule.MondayStart:
            total_hours += (schedule.MondayEnd - schedule.MondayStart)
        # Tuesday
        if schedule.TuesdayEnd >= schedule.TuesdayStart:
            total_hours += (schedule.TuesdayEnd - schedule.TuesdayStart)
        # Wednesday
        if schedule.WednesdayEnd >= schedule.WednesdayStart:
            total_hours += (schedule.WednesdayEnd - schedule.WednesdayStart)
        # Thursday
        if schedule.ThursdayEnd >= schedule.ThursdayStart:
            total_hours += (schedule.ThursdayEnd - schedule.ThursdayStart)
        # Friday
        if schedule.FridayEnd >= schedule.FridayStart:
            total_hours += (schedule.FridayEnd - schedule.FridayStart)
        # Saturday
        if schedule.SaturdayEnd >= schedule.SaturdayStart:
            total_hours += (schedule.SaturdayEnd - schedule.SaturdayStart)

        
        return total_hours
        

    for schedule in schedules:
        Schedule.objects.filter(id=schedule.id).update(TotalTime = getTime(schedule))
        
        


    return render(request, 'home.html', {
    'schedules': schedules, 
    'sunday_availability': sunday_availability, 
    'monday_availability': monday_availability, 
    'tuesday_availability': tuesday_availability, 
    'wednesday_availability': wednesday_availability, 
    'thursday_availability': thursday_availability, 
    'friday_availability': friday_availability, 
    'saturday_availability': saturday_availability,
    'total_openings': total_openings,
    'total_users': total_users,
    'total_hours_by_user': total_hours_by_user
    
    })

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
