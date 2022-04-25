from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from datetime import date

# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    is_lecturer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_photo = CloudinaryField('image')
    date_joined = models.DateTimeField(auto_now_add=True)


    def save_user(self):
        self.save()

    def update_user(self):
        self.update()

    def delete_user(self):
        self.delete()

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)

    def __str___(self):
        return self.phone

    def __str__(self):
        return self.user.username
        
class Semester(models.Model):
    semester_name   =   models.CharField(help_text='Eg- 1.1,2.2,4.1,5.2 etc', max_length=100) 
    creation_date =   models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.semester_name

class Student(models.Model):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT,primary_key=True)
    regno = models.CharField(help_text='Eg- sct-121,sct-220,sct-560etc',max_length=100,unique=False)
    email = models.EmailField()
    gender = models.CharField(max_length=8, choices=select_gender)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,null=True)
    # unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.regno


class Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_code = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_name

class Results(models.Model):
    name =models.CharField(max_length=100)
    marks = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.user.first_name

class RegisterUnits(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit.unit_name