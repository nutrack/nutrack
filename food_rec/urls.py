from django.urls import path
from food_rec.views import show_all_food, show_user_food, add_food_ajax, rate_food_ajax, show_food_food, show_json

app_name = 'food_rec'

urlpatterns = [
    path('', show_all_food, name='show_all_food'),
    path('add/', add_food_ajax, name='add_food_ajax'),
    path('json/', show_json, name='show_json'),
]