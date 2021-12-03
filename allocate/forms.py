from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

from allocate.models import Attendance


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2', 
        ]
        widgets = {
            'username': widgets.TextInput(attrs={'placeholder': "Username"}),
            'first_name': widgets.TextInput(attrs={'placeholder': "First Name"}),
            'last_name': widgets.TextInput(attrs={'placeholder': "Last Name"}),
            'email': widgets.EmailInput(attrs={'placeholder': "example@example.com"}),
            'password1': widgets.PasswordInput(attrs={'placeholder': "Password"}),
            'password2': widgets.PasswordInput(attrs={'placeholder': "Repeat Password"}),
        }

class LoginForm(AuthenticationForm):
    fields = '__all__'
    widgets = {
        'username': widgets.TextInput(attrs={'placeholder': "Username"}),
        'password': widgets.PasswordInput(attrs={'placeholder': "Password"}),
    }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['action', 'date', 'time']
        widgets = {
            'date': widgets.TextInput(attrs={'type': 'date'}),
            'time': widgets.TextInput(attrs={'type': 'time'})
        }
