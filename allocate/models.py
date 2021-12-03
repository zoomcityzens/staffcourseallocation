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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Name: {0} {1}|Job Title {2}".format(
            self.user.first_name, 
            self.user.last_name, 
            self.job_title
        )
    
    
class Allocation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    facilitator = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    duration = models.CharField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "staff: {0} {1} |username: {2} | course: {3}".format(
            self.staff.user.first_name,
            self.staff.user.last_name,
            self.staff.user.username,
            self.course
        )

class Attendance(models.Model):
    ACTIONS = [
        ('SIGN IN', 'SIGN IN'),
        ('SIGN OUT', 'SIGN OUT'),
    ]
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=8, choices=ACTIONS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    timestamp = models.DateTimeField(auto_now_add=timezone.now)

    def __str__(self) -> str:
        return "{0} {1} | {2} {3} | {4}".format(
            self.user.first_name,
            self.user.last_name,
            self.date,
            self.time,
            self.timestamp
        )
