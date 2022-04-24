from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

class ParentSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        parent = Parent.objects.create(user=user)
        parent.email = self.cleaned_data.get('email')

        parent.save()

        return parent

class StudentSignUp(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.email = self.cleaned_data.get('email')

        student.save()

        return student

class UpdateParentProfile(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('phone', 'profile_photo', )

class UpdateStudentProfile(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('regno', 'gender', 'email',
                  'semester')

class UpdateUserProfile(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'
        

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_name', 'unit_code', 'semester']
        
class ResultsForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = ['marks', 'unit', 'student', 'semester']      

class RegisterUnitsForm(forms.ModelForm):
    class Meta:
        model = RegisterUnits
        fields = ['student', 'unit']