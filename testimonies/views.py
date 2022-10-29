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
import datetime

def show_testimonies(request):
    data = Testimony.objects.all()
    context = {
        'data' : data
        }
    return render(request, "testimonies.html", context)