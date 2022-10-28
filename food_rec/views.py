from django.shortcuts import render
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import get_object_or_404, render
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from food_rec.models import Food
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
# Create your views here.

def show_all_food(request):
    foods = Food.objects.all()
    context = { 'foods': foods }
    return render(request, 'indexx.html', context)

@login_required(login_url='login')
def show_user_food(request):
    foods = Food.objects.filter(user=request.user)
    context = { 'foods': foods }
    return render(request, 'food_rec/show_user_food.html', context)

@login_required(login_url='login')
def add_food_ajax(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        protein = request.POST['protein']
        fat = request.POST['fat']
        carbs = request.POST['carbs']
        is_food = request.POST['is_food']
        rating = request.POST['rating']
        food = Food.objects.create(user=request.user, name=name, calories=calories, protein=protein, fat=fat, carbs=carbs, is_food=is_food, rating=rating)
        result = {
            'fields': {
                'name': food.name,
                'calories': food.calories,
                'protein': food.protein,
                'fat': food.fat,
                'carbs': food.carbs,
                'is_food': food.is_food,
                'rating': food.rating,
            },
            'pk': food.pk
        }
        return JsonResponse("Success")
    else:
        return HttpResponseBadRequest()

@login_required(login_url='login')
def rate_food_ajax(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        rating = request.POST['rating']
        food = Food.objects.get(pk=pk)
        food.rating = rating
        food.save()
        return JsonResponse("Success")
    else:
        return HttpResponseBadRequest()

def show_food_food(request):
    foods = Food.objects.filter(is_food=True)
    context = { 'foods': foods }
    return render(request, 'food_rec/show_food_food.html', context)

def sort_food(request):
    foods = Food.objects.filter(is_food=True).order_by('-rating')
    context = { 'foods': foods }
    return render(request, 'indexx.html', context)

def sort_food_by_name(request):
    foods = Food.objects.filter(is_food=True).order_by('name')
    context = { 'foods': foods }
    return render(request, 'food_rec/show_food_food.html', context)