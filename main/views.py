from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponse, HttpRequest
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.backends import UserModel
from django import forms
from main.models import Nutrack

from main.forms import CreateUserForm
import sys

# adding nutrack/calorycalc to the system path
sys.path.insert(0, '/nutrack/calorycalc/')

# import caloryInfo
from calorycalc.models import caloryInfo

# Create your views here.
# @login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')

def choose_user(request:HttpRequest):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("main:caloryInfo"))
    return HttpResponseRedirect(reverse("main:home"))
    

@login_required(login_url='/login/')
def show_calory_info(request):
    data_calory = caloryInfo.objects.filter(user=request.user).all()
    context = {
        'get_calory': data_calory,
    }
    return render(request, 'index.html', context)
    

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('main:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("main:home")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:home'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login/')
def calorycalc_json(request):
    data = caloryInfo.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def about(request):
    context = {}
    return render(request, 'about.html', context)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Nutrack
        fields= ['goal']

def add_cal_goal(request):
    form = TaskForm(request.POST)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        return JsonResponse({'goal':form.instance.goal,"id":form.instance.pk})
    return redirect("main:caloryInfo")

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "username": request.user.username,
              "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data["username"]
        email = data["email"]
        password1 = data["password1"]

        newUser = UserModel.objects.create_user(
        username = username, 
        email = email,
        password = password1,
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def logout_flutter(request):
    try:
        logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged out!"
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)