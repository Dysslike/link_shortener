from django.shortcuts import render, redirect
from .forms import signupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.
def base(request):
    return render(request, "link/index.html")

def dashboard(request):
    return render(request, "link/pages/dashboard.html")

def home(request):
    return render(request, "link/pages/home.html")

def landing(request):
    return render(request, "link/pages/landing.html")

def account(request):
    return render(request, "link/pages/account.html")

def signup(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,"Successfully created an account")
        return redirect("login")
    else:
        form = signupForm()
    return render(request, "link/pages/signup.html", {"form":form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request,"Successfully Logged in")
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect("landing")

def get_username_index(request):
    username = request.user.username
    return render(request, "index.html",{"username":username})

@login_required
def get_user_details(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    return render(request,"account.html",{
                  "first_name":first_name,
                  "last_name":last_name,
                  "email":email
                  })