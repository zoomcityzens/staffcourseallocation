from django.shortcuts import render
from .models import Staff, Course, Allocation

 
def home(request):
    return render(request, 'allocate/home.html')

def allocation(request):
    courses = Course.objects.all()
    context = {'courses': courses }
    return render(request, 'allocate/allocation.html', context)

def coursedetails(request):
    allocations = Allocation.objects.all()
    context = {'allocations': allocations }
    return render(request, 'allocate/coursedetails.html', context)

