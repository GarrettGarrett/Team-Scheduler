from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('new/', views.new),
    path('new/', views.ScheduleCreate.as_view()),
    path('<int:pk>/update', views.ScheduleUpdate.as_view()),
    path('<int:pk>/delete', views.ScheduleDelete.as_view()),

]