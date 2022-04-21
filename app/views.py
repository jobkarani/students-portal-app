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


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student Creation'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Create Student'
        return context

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    field_list = [
        'Student Name', 'Roll No', 'Class', 'Reg Date', 'Date of birth'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Students'
        context['panel_name']   =   'Students'
        context['panel_title']  =   'View Students Info'
        context['field_list']   =   self.field_list
        return context

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name_suffix = '_form'
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Update Student Info'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Update Student info'
        return context

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name_suffix = '_delete'
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student Delete Confirmation'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Delete Student'
        return context
class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Unit
    form_class = UnitForm
    
    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Creation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Add Subject'
        return context

class SubjectListView(LoginRequiredMixin, ListView):
    model = Unit
    field_list = [
        'Subject Name', 'Subject Code', 'Creation Date', 'Last Updated'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Subjects'
        context['panel_name']   =   'Subjects'
        context['panel_title']  =   'View Subjects Info'
        context['field_list']   =   self.field_list
        return context

class SubjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Unit
    template_name_suffix = '_form'
    form_class = UnitForm
    success_url = reverse_lazy('subjects:subject_list')

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Unit
    template_name_suffix = '_delete'
    success_url = reverse_lazy('subjects:subject_list')

    
    def get_context_data(self, **kwargs):
        context = super(SubjectDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Delete Confirmation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Delete Subject'
        return context
    
class StudentClassCreateView(LoginRequiredMixin, CreateView):
    model = StudentClass
    form_class = StudentClassForm

    
    def get_context_data(self, **kwargs):
        context = super(StudentClassCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Add Student Class'
        context['panel_name'] = 'Classes'
        context['panel_title'] = 'Add Class'
        return context

class StudentClassListView(LoginRequiredMixin, ListView):
    model = StudentClass

    field_list = [
        'Class Name', 'Class Name In Numeric', 'Section', 'Creation Date'
    ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Classes'
        context['panel_name']   =   'Classes'
        context['panel_title']  =   'View Classes Info'
        context['field_list']   =   self.field_list
        return context

class StudentClassUpdateView(LoginRequiredMixin, UpdateView):
    model = StudentClass
    form_class = StudentClassForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('student_classes:class_list')

class StudentClassDeleteView(LoginRequiredMixin, DeleteView):
    model = StudentClass
    template_name_suffix = '_delete'
    success_url = reverse_lazy('student_classes:class_list')

    def get_context_data(self, **kwargs):
        context = super(StudentClassDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Class Delete Confirmation'
        context['panel_name'] = 'Classes'
        context['panel_title'] = 'Delete Class'
        return context

