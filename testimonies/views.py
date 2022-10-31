from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from urllib import response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Testimony
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import TestimonyForm
import datetime

def show_testimonies(request):
    data = Testimony.objects.all()
    context = {
        'data' : data
        }
    return render(request, "testimonies.html", context)

def create_testimonies(request):
    user = request.user
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect('testimonies:show_testimonies')

    context = {}
    return render(request, 'create-testimonies.html', context)