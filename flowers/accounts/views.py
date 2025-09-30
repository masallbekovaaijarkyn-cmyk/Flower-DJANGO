from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def signup(request):
    # jdakjjksad
    if request.method == "POST":
        # djfljdsfjjs
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user=user) #
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html",
                  {"form": form})

@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile.html",
                  {"form": form, "profile": profile})
