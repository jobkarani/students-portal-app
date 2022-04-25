from datetime import datetime
import pandas
from django.views.generic import ListView
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse,HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import *
from datetime import datetime as datetime
from django.db.models import Sum
from django.http import HttpResponse
# from django.core.files.storage import FileSystemStorage
from django.views.generic import View
from . import models
from .process import render_to_pdf
# from django.template.loader import render_to_string

# Create your views here.

def index(requests):
    return render(requests, "all-temps/index.html")

def options(request):
    return render(request, 'registration/options.html')


@login_required
def profileStudent(request, id):
    student = User.objects.get(id=id)
    profile = Student.objects.get(user_id=id)  # get profile
    return render(request, "student/student.html", {"student": student, "profile": profile})

@login_required
def update_student_profile(request):
    current_user = request.user
    profile = Student.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        user_form = UpdateUserProfile(
            request.POST, request.FILES, instance=request.user)
        student_form = UpdateStudentProfile(
            request.POST, request.FILES, instance=request.user.student)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            messages.success(
                request, 'Your Profile account has been updated successfully')
            return redirect('profileStudent')
    else:
        user_form = UpdateUserProfile(instance=request.user)
        student_form = UpdateStudentProfile(
            instance=request.user.student)
    params = {
        'user_form': user_form,
        'student_form': student_form,
        'profile': profile
    }
    return render(request, 'student/update_student.html', params)

@login_required
def delete_student(request, user_id):
    student = Student.objects.get(pk=user_id)
    if student:
        student.delete_user()
        messages.success(request, f'User deleted successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def parentProfile(request):
    parent = request.user
    profile = Parent.objects.get(user_id=parent.id)  # get profile
    profile = Parent.objects.filter(
        user_id=parent.id).first()  # get profile
    context = {
        "parent": parent,
        'profile': profile
    }
    return render(request, 'parent/parent.html', context)

@login_required
def update_parent_profile(request):
    current_user = request.user
    profile = Parent.objects.get(
        user_id=current_user.id)  # get profile
    if request.method == 'POST':
        u_form = UpdateUserProfile(
            request.POST, request.FILES, instance=request.user)
        p_form = UpdateParentProfile(
            request.POST, request.FILES, instance=request.user.parent)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, 'Your Profile account has been updated successfully')
            return redirect('profile')
    else:
        u_form = UpdateUserProfile(instance=request.user)
        p_form = UpdateParentProfile(instance=request.user.parent)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile
    }
    return render(request, 'parent/update_parent.html', context)

@login_required
def delete_parent(request, user_id):
    parent = Parent.objects.get(pk=user_id)
    if parent:
        parent.delete_user()
        messages.success(request, f'Parent deleted successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def student_signup(request):
    if request.method == "POST":
        form = StudentSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = StudentSignUp()
    return render(request, "django_registration/registration_form.html", {'form': form})

def parent_signup(request):
    if request.method == "POST":
        form = ParentSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = ParentSignUp()
    return render(request, "django_registration/registration_form.html", {'form': form})

def parent_home(request):
    return render(request, 'parent/home.html')


def student_home(request):
    return render(request, 'student/home.html')

@login_required
def dashboard(request):
    current = request.user
    if current.is_parent:
        return redirect('parentDash/')
    elif current.is_lecturer:
        return redirect('lecturerdashboard')
    else:
        return redirect('studentDash/')

@login_required
def lecturerDash(request):
    all_parents = User.objects.filter(is_parent=True).all()
    all_students = User.objects.filter(is_student=True).all()
    
    return render(request, 'lecturer/lecturer_dashboard.html', {"all_parents": all_parents, 'all_students': all_students})

# @login_required
# def parentDash(request):
#     current_user = request.user
#     profile = Parent.objects.get(user_id=current_user.id)
#     student = User.objects.filter(is_student=True).all()
#     student_profs = Student.objects.all()
#     parent = User.objects.all()
    
#     context = {
#         "student": student,
#         "parent": parent,
#         'profile': profile,
#         'student_profs':student_profs,
    
#     }
#     return render(request, 'parent/parent_dashboard.html', context)


def search_student(request):
    current_user = request.user
    profile = Parent.objects.get(user_id=current_user.id)
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_students = Student.search_students_by_user(
            search_term)
        message = f"{search_term}"

        return render(request, 'parent/search.html', {"message": message, "students": searched_students, 'profile': profile})

    else:
        message = 'You have not searched for any term'
        return render(request, 'parent/search.html', {"message": message, })


def createStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    print(form)
    return render(request, 'all-temps/student_form.html', {"form":form})

def viewStudents(request):
    students = Student.objects.filter().all()
    print(students)
    ctx ={
        "students":students,
    }
    return render(request, 'all-temps/students.html',ctx)

def createUnit(request):
    # current_user = request.user
    # if current_user == 'is_student':
    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UnitForm()
    print(form)
    return render(request, 'all-temps/unit_form.html', {"form":form})
    # else:
    #     return HttpResponse('You must be signed in as a student to perform this action.')

def viewUnits(request):
    units = Unit.objects.filter().all()
    print(units)
    ctx ={
        "units":units,
    }
    return render(request, 'all-temps/units.html',ctx)

def removeUnit(request, slug):
    current_user = request.user
    if current_user == 'is_student':
        unit = get_object_or_404(Unit, unit_name=slug)
        unit.delete()
        ctx ={
            "unit":unit,
        }
        return redirect('viewUnits')
    else:
        return HttpResponse('You must be signed in as a student to perform this action.')

def createSem(request):
    # current_user = request.user
    # if current_user == 'is_student':
    if request.method == 'POST':
        form = SemesterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SemesterForm()
    # else:
    #     return HttpResponse('You must be signed in as a student to perform this action.')
    print(form)
    return render(request, 'all-temps/sem_form.html', {"form":form})

def viewSems(request):
    sems = Semester.objects.filter().all()
    print(sems)
    ctx ={
        "sems":sems,
    }
    return render(request, 'all-temps/semesters.html',ctx)

def removeSem(request, slug):
    current_user = request.user
    if current_user == 'is_student':
        sems = get_object_or_404(Semester, semester_name=slug)
        sems.delete()
        ctx ={
            "sems":sems,
        }
        return redirect('viewSems')
    else:
        return HttpResponse('You must be signed in as a student to perform this action.')

def createResults(request):
    # current_user = request.user
    # if current_user == 'is_student':
    if request.method == 'POST':
        form = ResultsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ResultsForm()
    # else:
    #     return HttpResponse('You must be signed in as a student to perform this action.')
    print(form)
    return render(request, 'all-temps/results_form.html', {"form":form})

def viewResults(request):
    marks = Results.objects.filter().all()
    print(marks)
    ctx ={
        "marks":marks,
    }
    return render(request, 'all-temps/results.html' ,ctx)

def viewPdfResults(request):
    marks = Results.objects.filter().all()
    print(marks)
    ctx ={
        "marks":marks,
    }
    return render(request, 'all-temps/result.html' ,ctx)

def bar_chart(request):
    labels = []
    data = []

    queryset = Results.objects.values('semester__semester_name','unit__unit_name').annotate(result_marks=Sum('marks')).order_by('-result_marks')
    for entry in queryset:
        labels.append(entry['semester__semester_name'])
        labels.append(entry['unit__unit_name'])
        data.append(entry['result_marks'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def registerUnits(request):
    # current_user = request.user
    # if current_user == 'is_student':
        regUnitsForm = RegisterUnitsForm()
        if request.method == 'POST':
            regUnitsForm = RegisterUnitsForm(request.POST)
            if regUnitsForm.is_valid():
                regUnits = regUnitsForm.save(commit=True)
                regUnits.save()
                return redirect("/")
            print("Error wirth form")
        return render(request, "all-temps/regunits.html", {"form":regUnitsForm})
    
    # else:
    #     return HttpResponse('You must be signed in as a student to perform this action.')

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = models.Results.objects.all().order_by('name')

        ctx = {
            "data":data,
        }
        print(data)
        pdf = render_to_pdf('all-temps/result.html',ctx)
        return HttpResponse(pdf, content_type='application/pdf')
