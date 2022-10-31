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
from food_rec.forms import FoodForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
# Create your views here.

def show_all_food(request):
    foods = Food.objects.all()
    context = { 'foods': foods}
    return render(request, 'indexx.html', context)

@login_required(login_url='/login/')
def show_user_food(request):
    foods = Food.objects.filter(user=request.user)
    context = { 'foods': foods }
    return render(request, 'indexx_user.html', context)

def show_json(request):
    foods = Food.objects.all()
    data = serializers.serialize('json', foods)
    return HttpResponse(data, content_type='application/json')

# Show Article Page by ID #
def food_page_by_id(request, id):
    data = Food.objects.get(id=id)
    context = {
        'food': data,
        'id': id,
        'username': request.user.username,
    }
    return render(request, 'food-detail.html', context)

def add_food_page(request):
    return render(request, 'add-food.html')

@csrf_exempt
def add_food_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        protein = request.POST.get('protein')
        fat = request.POST.get('fat')
        carbs = request.POST.get('carbs')
        print(request.POST.get('is_food'))
        is_food = bool(request.POST.get('is_food'))
        print(is_food)
        rating = request.POST.get('rating')
        if int(rating) > 5:
            rating = 5
        food = Food.objects.create(user= request.user, name=name, calories=calories, protein=protein, fat=fat, carbs=carbs, rating=rating, is_food=is_food)
        result = {
            'fields': {
                'name': name,
                'calories': calories,
                'protein': protein,
                'fat': fat,
                'carbs': carbs,
                'rating': rating,
                'is_food': is_food,
            },
            'pk': food.pk
        }
        return JsonResponse(result)
    else:
        return HttpResponseBadRequest()

# @login_required(login_url='/login/')
# def rate_food_ajax(request):
#     if request.method == 'POST':
#         pk = request.POST['pk']
#         rating = request.POST['rating']
#         food = Food.objects.get(pk=pk)
#         food.rater += 1
#         food.rating = (food.rating * (food.rater - 1) + int(rating)) / food.rater
#         food.rating = rating
#         food.save()
#         return HttpResponseRedirect(reverse('food_rec:show_all_food'))
#     else:
#         return HttpResponseBadRequest()

def show_food_food(request):
    foods = Food.objects.filter(is_food=True)
    context = { 'foods': foods }
    return render(request, 'indexx.html', context)

def sort_food(request):
    foods = Food.objects.order_by('-rating')
    context = { 'foods': foods }
    return render(request, 'indexx.html', context)

def sort_food_by_name(request):
    foods = Food.objects.order_by('name')
    context = { 'foods': foods }
    return render(request, 'indexx.html', context)