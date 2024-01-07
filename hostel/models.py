\
from django.db import models

# Create your models here.


class Hostel(models.Model):
    hostel_name = models.CharField(max_length=30,primary_key=True)
    no_of_vacancy = models.IntegerField()    
    no_of_students = models.IntegerField()

    def __str__(self):
        return self.hostel_name
    

class student(models.Model):
    student_id = models.IntegerField(primary_key=True) 
    student_name = models.CharField(max_length=30)      
    student_semester = models.IntegerField()
    student_year = models.CharField(max_length=30)
    student_email = models.CharField(max_length=30)
    student_branch = models.CharField(max_length = 30)
    student_phone = models.IntegerField()
    student_age = models.IntegerField()
    address_area = models.CharField(max_length = 100)
    address_city = models.CharField(max_length = 40)
    address_state = models.CharField(max_length = 40)    
    student_start_date=models.DateField()
    student_end_date=models.DateField()
    student_application_status= models.CharField(max_length=30,default="Applied")   
    hostel_name = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
     return self.student_name
    

class Admin (models.Model):
   Username =models.CharField(max_length=30,primary_key=True)
   Admin_name =models.CharField(max_length=30)
   password = models.CharField(max_length=30)   

   def __str__(self):
        return self.Admin_name





