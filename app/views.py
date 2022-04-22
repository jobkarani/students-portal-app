from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import *

# Create your views here.

def index(requests):
    return render(requests, "all-temps/index.html")

@login_required(login_url="/accounts/login/")
def create_profile(request):
    current_user = request.user
    title = "CreateProfile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = ProfileForm()
    return render(request, 'all-temps/create_profile.html', {"form": form, "title": title})




@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
    else:
        form = ProfileForm()
    return render(request, "all-temps/profile.html", {"profile": profile, "form":form})



def update_profile(request, id):
    # current_user = request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    ctx = {
        "form": form,
        "user":user,
        "profile":profile,
        }
    return render(request, 'all-temps/update_profile.html', ctx)

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

    return render(request, 'all-temps/units.html')

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

    return render(request, 'all-temps/semesters.html')

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

    return render(request, 'all-temps/results.html')