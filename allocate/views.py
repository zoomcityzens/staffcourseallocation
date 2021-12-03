from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Attendance, Staff, Course, Allocation
from .forms import AttendanceForm, CreateUser

 
def home(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        if (form := AuthenticationForm(request.POST)).is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username != "" and password != "":
                user = authenticate(request, username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return redirect('allocation')
            for form_error in form.error_messages.values():
                messages.error(request, form_error)
                
    context = {'form': form}
    return render(request, 'allocate/home.html', context)

def allocation(request):
    context = {'allocations': Allocation.objects.all() }
    return render(request, 'allocate/allocation.html', context)

def coursedetails(request, pk):
    context = {'allocation': Allocation.objects.get(pk=pk) }
    return render(request, 'allocate/coursedetails.html', context)

def create_user(request):
    template_name = 'allocate/registration.html'
    form = CreateUser()
    if request.method == 'POST':
        if (form := CreateUser(request.POST)).is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, form.error_messages)
    context = {'form': form}
    return render(request, template_name, context)

def take_attendance(request):
    template_name = "allocate/attendance.html"
    if request.method == 'POST':
        if (form := AttendanceForm(request.POST)).is_valid():
            form.instance.user = request.user
            form.instance.allocation = Allocation.objects.get(staff=request.user)
            form.save()
    context = {
        'form': AttendanceForm(),
    }
    return render(request, template_name, context)

