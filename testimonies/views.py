from this import d
from urllib import response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import Testimony
# Create your views here.
def testimonies_json(request):
    data = Testimony.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = 'application/json')

def show_testimonies(request):
    data = Testimony.objects.all()
    username = request.user.username
    context = {
        "username": username,
        "data": data
    }
    return render(request, "testimonies.html", context)

@login_required("/login/")
def create_testimony(request):
    user = request.user

    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        Testimony.objects.create(user=user, title=title, testimony=desc)
        return HttpResponseRedirect(reverse("testimonies:testimonies"))
    pass