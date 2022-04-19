from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import *

# Create your views here.

def index(requests):
    return render(requests, "all-temps/index.html")

@login_required(login_url="/accounts/login/")
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')
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
    return render(request, "all-temps/profile.html", {"profile": profile})



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
    return render(request, 'all-temps/update_prof.html', ctx)
