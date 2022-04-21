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
        exclude = ['student_reg']
        widgets = {
            'name'  :   forms.TextInput(attrs={'class':'form-control'}),
            'roll'  :   forms.NumberInput(attrs={'class':'form-control'}),
            'email'  :   forms.EmailInput(attrs={'class':'form-control'}),
            'gender'  :   forms.Select(attrs={'class':'form-control'}),
            'class'  :   forms.Select(attrs={'class':'form-control'}),
            'dob'  :   forms.DateInput(attrs={'class':'form-control'}),
        }


class StudentClassForm(ModelForm):
    class Meta:
        model = StudentClass
        exlude  =   'creation_date'
        fields = '__all__'
        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'form-control'}),
            'class_name_in_numeric':  forms.NumberInput(attrs={'class': 'form-control'}),
            'section':  forms.TextInput(attrs={'class': 'form-control'}),
        }