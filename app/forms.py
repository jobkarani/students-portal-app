from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'email', 'phone']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        


class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'
        

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_name', 'unit_code', 'semester']
        
class ResultsForm(ModelForm):
    class Meta:
        model = Results
        fields = ['marks', 'unit', 'student', 'semester']      