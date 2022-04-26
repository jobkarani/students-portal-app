from datetime import datetime
import re
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

def aboutUs(request):
    return render(request, 'aboutus.html')

def dashboard(request):
    return render (request,'all-temps/dashboard.html')

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



def createStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createStudent')
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
    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createUnit')
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
        form = TermForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createSem')
    else:
        form = TermForm()
    print(form)
    return render(request, 'all-temps/sem_form.html', {"form":form})

def viewSems(request):
    sems = Term.objects.filter().all()
    print(sems)
    ctx ={
        "sems":sems,
    }
    return render(request, 'all-temps/semesters.html',ctx)

def removeSem(request, slug):
        sems = get_object_or_404(Term, term_name=slug)
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
            return redirect('createResults')
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

    queryset = Results.objects.values('term__term_name').annotate(result_marks=Sum('marks')).order_by('-result_marks')
    for entry in queryset:
        labels.append(entry['term__term_name'])
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
    
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = models.Results.objects.all().order_by('name')

        ctx = {
            "data":data,
        }
        print(data)
        pdf = render_to_pdf('all-temps/result.html',ctx)
        return HttpResponse(pdf, content_type='application/pdf')
