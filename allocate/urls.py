from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('allocation/', views.allocation, name="allocation"),
    path('coursedetails/<pk>/', views.coursedetails, name="coursedetails"),
    path('registeration/', views.create_user, name="registration"),
    path('attendance/', views.take_attendance, name="attendance"),
] 