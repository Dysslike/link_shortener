from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, "link/index.html")

def dashboard(request):
    return render(request, "link/pages/dashboard.html")

def home(request):
    return render(request, "link/pages/home.html")

def landing(request):
    return render(request, "link/pages/landing.html")

def signup(request):
    return render(request, "link/pages/signup.html")

def login(request):
    return render(request, "link/pages/login.html")