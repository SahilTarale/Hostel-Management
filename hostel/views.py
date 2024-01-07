from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from .models import student,Hostel,Admin
from django.utils import timezone

# Create your views here.

def home(request) :
    return render(request, 'home.html')

def form(request):
    hostels = Hostel.objects.all()
    return render(request, 'form.html',{'hostels':hostels})


def application_submit(request) :
    
    
    if request.method=='POST':
        student_name=request.POST.get('student_name')
        student_id=request.POST.get('student_id')
        student_semester=request.POST.get('student_semester')
        student_year=request.POST.get('student_year')
        student_email=request.POST.get('student_email')
        student_branch=request.POST.get('student_branch')
        student_phone=request.POST.get('student_phone')
        student_age=request.POST.get('student_age')
        address_area=request.POST.get('student_address')
        address_city=request.POST.get('student_city')
        address_state=request.POST.get('student_state')
        student_hostel=request.POST.get('student_hostel')
        student_start_date=request.POST.get('student_start_date')
        student_end_date=request.POST.get('student_end_date')

        try:
            hostel_instance = Hostel.objects.get(hostel_name=student_hostel)

        except Hostel.DoesNotExist:
            
            return HttpResponse("Invalid Hostel Name")
        
        Student=student(student_name=student_name,
                         student_id=student_id,
                         student_semester=student_semester,
                         student_year=student_year,
                         student_email=student_email,
                         student_branch=student_branch,
                         student_phone=student_phone,
                         student_age=student_age,
                         address_area=address_area,
                         address_city=address_city,
                         address_state=address_state,
                         hostel_name=hostel_instance,
                         student_start_date=student_start_date,
                         student_end_date=student_end_date
                         )
        
        Student.save()

    return render(request, 'application_submit.html')




#admin functionality



def admin_page(request):
    student_applications = student.objects.filter(student_application_status='Applied')
    hostels = Hostel.objects.all()
    return render(request, 'admin_page.html', {'student_applications': student_applications, 'hostels': hostels})

def accept_applications(request):
    if request.method == 'POST':
        student_ids = request.POST.getlist('student_id')
        hostel_names = request.POST.getlist('hostel_name')

        for student_id, hostel_name in zip(student_ids, hostel_names):
            student_application = get_object_or_404(student, pk=student_id)

           
            student_application.student_application_status = 'Accepted'
            # student_application.hostel_name = hostel_name
            student_application.save()

           
            hostel = get_object_or_404(Hostel, pk=hostel_name)
            hostel.no_of_vacancy -= 1
            hostel.no_of_students+=1
            hostel.save()

        return render(request, 'applications_accepted.html')

    return render(request, 'admin_page.html', {'error_message': 'Invalid request'})




def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        admin_user = Admin.objects.filter(Username=username, password=password).first()

        if admin_user:
            messages.success(request, 'Successfully logged in as admin.')
            
            return redirect('admin_page')  
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'admin_login.html')


def expire_allotment(request):
    student_alloteds = student.objects.all()
    
    for student_alloted in student_alloteds:
        if student_alloted.student_end_date < timezone.now().date():
            student_alloted.student_application_status = 'expire'
            student_alloted.save()

    return render(request, 'admin_page.html')
    
  

        
        

        


