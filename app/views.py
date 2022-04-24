from datetime import datetime
import pandas
from django.views.generic import ListView
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import *
from datetime import datetime as datetime
from django.db.models import Sum
from django.http import JsonResponse

# Create your views here.

def index(requests):
    return render(requests, "all-temps/index.html")

# @login_required(login_url="/accounts/login/")
# def create_profile(request):
#     current_user = request.user
#     title = "CreateProfile"
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = current_user
#             profile.save()
#     else:
#         form = ProfileForm()
#     return render(request, 'all-temps/create_profile.html', {"form": form, "title": title})


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



# def update_profile(request, id):
#     # current_user = request.user
#     user = User.objects.get(id=id)
#     profile = Profile.objects.get(user=user)
#     form = UpdateProfileForm(instance=profile)
#     if request.method == "POST":
#         form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():

#             profile = form.save(commit=False)
#             profile.save()
#             return redirect('profile')

#     ctx = {
#         "form": form,
#         "user":user,
#         "profile":profile,
#         }
#     return render(request, 'all-temps/update_profile.html', ctx)

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

def createUnit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UnitForm()
    print(form)
    return render(request, 'all-temps/unit_form.html', {"form":form})

def viewUnits(request):
    units = Unit.objects.filter().all()
    print(units)
    ctx ={
        "units":units,
    }
    return render(request, 'all-temps/units.html',ctx)

def removeUnit(request, slug):
    unit = get_object_or_404(Unit, unit_name=slug)
    unit.delete()
    ctx ={
        "unit":unit,
    }
    return redirect('viewUnits')

def createSem(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SemesterForm()
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
    sems = get_object_or_404(Semester, semester_name=slug)
    sems.delete()
    ctx ={
        "sems":sems,
    }
    return redirect('viewSems')

def createResults(request):
    if request.method == 'POST':
        form = ResultsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ResultsForm()
    print(form)
    return render(request, 'all-temps/results_form.html', {"form":form})

def viewResults(request):
    marks = Results.objects.filter().all()
    print(marks)
    ctx ={
        
        "marks":marks,
    }
    return render(request, 'all-temps/results.html',ctx)

def bar_chart(request):
    labels = []
    data = []

    queryset = Results.objects.values('semester__semester_name').annotate(result_marks=Sum('marks')).order_by('-result_marks')
    for entry in queryset:
        labels.append(entry['semester__semester_name'])
        data.append(entry['result_marks'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def registerUnits(request):
    regUnitsForm = RegisterUnitsForm()
    if request.method == 'POST':
        regUnitsForm = RegisterUnitsForm(request.POST)
        if regUnitsForm.is_valid():
            regUnits = regUnitsForm.save(commit=True)
            regUnits.save()
            return redirect("/")
        print("Error wirth form")
    return render(request, "all-temps/regunits.html", {"form":regUnitsForm})
