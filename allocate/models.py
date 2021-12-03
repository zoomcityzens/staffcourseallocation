from django.db import models
from django.utils import timezone
from uuid import uuid4
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

class Attendance(models.Model):
    ACTIONS = [
        ('SIGN IN', 'SIGN IN'),
        ('SIGN OUT', 'SIGN OUT'),
    ]
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    action = models.CharField(max_length=8, choices=ACTIONS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    timestamp = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self) -> str:
        return f"{0} {1} | {2} {3} \n {4}".format(
            self.user.first_name,
            self.user.last_name,
            self.date,
            self.time,
            self.timestamp
        )
