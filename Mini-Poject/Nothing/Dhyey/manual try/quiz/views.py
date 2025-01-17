from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *


# Create your views here.


def home(request):
    return render(request, 'quiz/index (1).html')
def home2(request):
    return render(request, 'quiz/home.html')


def login(request):

    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['password']
        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)
        return redirect('home2')
    
    return render(request, 'registration/login.html')





def register(request):

    if request.method == "POST":
        username = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        submit = request.POST['submit']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "This email is already registered! Please try to Login :) ")
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, "User already exist with the same username!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()

                user_login = auth.authenticate(username=username, password1=password1)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, email=email)
                new_profile.save()
                # return redirect('home')
                return render(request, 'quiz/home.html')
            
        else:
            messages.info(request, "Password not matching!")
            return redirect('register')

    context = {}
    return render(request, 'registration/register.html', context)