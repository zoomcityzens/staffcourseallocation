from django.contrib import admin
from .models import Staff, Course, Allocation

# Register your models here.

class AdminAllocation(admin.ModelAdmin):
    model = Allocation
    list_display = ('staff', 'course', 'description', 'facilitator', 'location', 'duration')



admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Allocation, AdminAllocation)
