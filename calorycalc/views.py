from calorycalc.models import caloryInfo
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse  
# Create your views here.

def test(request):
    return render(request,"test.html")


@login_required(login_url='/login/')
def calorycalc(request):
    data=caloryInfo.objects.filter(user=request.user)
    context = {
    'calory' : data,
    }
    return render(request, "calorycalc.html", context)