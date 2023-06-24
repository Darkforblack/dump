from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser #Create your models here.

# Create your models here
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class NewUser(AbstractUser):
    USER_TYPE_CHOICES = (
        
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('receptionist', 'receptionist'),
    )
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, default='student')
    experience = models.CharField(max_length=300)

class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Course_student(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    selected_course=models.ForeignKey(Course,on_delete=models.CASCADE)
    paid_amount = models.CharField(max_length=300)
    
class Student_course_fee(models.Model):
    user=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    course_fee = models.CharField(max_length=300)
    paid_amount = models.CharField(max_length=300)
    # student_id=models.ForeignKey(NewUser,on_delete=models.CASCADE)
    selected_course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
   
    