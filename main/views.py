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