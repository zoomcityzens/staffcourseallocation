from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('allocation/', views.allocation, name="allocation"),
    path('coursedetails/', views.coursedetails, name="coursedetails"),
    
    ] 