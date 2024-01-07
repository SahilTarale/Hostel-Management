from django.contrib import admin

# Register your models here.
from .models import Hostel, student,Admin

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ['hostel_name', 'no_of_vacancy', 'no_of_students']

admin.site.register(student)
# @admin.register(student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['student_id','student_name', 'student_phone','student_branch', 'student_year','student_start_date','student_end_date','hostel_name']
#     list_filter = ['hostel_name','student_branch','student_year']
#     search_fields = ['student_name','student_id','student_branch']

@admin.register(Admin)
class CustomAdmin(admin.ModelAdmin):
    list_display=['Admin_name','Username','password']