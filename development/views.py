from django.shortcuts import render
import mysql.connector
from .forms import RegisterForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


# def register(request):
#     return render(request, 'register.html')

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'login.html', {'success': "Registration successfully. Please Login."})
        else:
            return render(request, 'register.html', {'form': form})
    return render(request,"register.html")

def login_view(request):
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard.html")
            else:
                messages.error(request, "Invalid email or password. Please try again.")
                return render(request, 'login.html')
        return render(request, "login.html")


@login_required(login_url="login")
def dashboard(request):
    return render(request, 'dashboard.html', {'name': request.user.first_name})

@login_required
def videocall(request):
    return render(request, 'videocall.html',{'name': request.user.first_name + " " + request.user.last_name})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")

@login_required
def join_room(request):
    return render(request, 'joinroom.html')

















