from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    jobTitle = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Allocation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    facilitator = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.staff)
  
    