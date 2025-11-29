from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, CustomUserForm

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("course:list_courses")
    form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "users/profile.html")


@login_required
def edit_profile_view(request):
    form = CustomUserForm(instance=request.user)
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("auth:profile")
    return render(request, "users/edit_profile.html", {"form": form})
