from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CareerGoal
from careers.models import Career
from .forms import ProfileForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def custom_logout(request):
    logout(request)
    return redirect("home")


@login_required
def set_goal(request, career_id):
    career = get_object_or_404(Career, id=career_id, is_active=True)
    CareerGoal.objects.update_or_create(
        user=request.user,
        defaults={"target_career": career, "progress": 0},
    )
    return redirect("my_goal")

@login_required
def my_goal(request):
    goal = CareerGoal.objects.filter(user=request.user).select_related("target_career").first()
    return render(request, "users/goal.html", {"goal": goal})

@login_required
def update_goal_progress(request, goal_id):
    goal = get_object_or_404(CareerGoal, id=goal_id, user=request.user)
    if request.method == "POST":
        progress = int(request.POST.get("progress", goal.progress))
        goal.progress = max(0, min(100, progress))  # clamp 0–100
        goal.save()
    return redirect("my_goal")


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("view_profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "users/edit_profile.html", {"form": form})

@login_required
def view_profile(request):
    return render(request, "users/view_profile.html", {"profile": request.user.profile})


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect("home")  # adjust to your homepage URL
    return render(request, "users/delete_account.html")

