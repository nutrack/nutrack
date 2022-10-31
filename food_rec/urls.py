from django.urls import path
from food_rec.views import show_all_food, show_user_food, add_food_ajax, rate_food_ajax, show_json, food_page_by_id, add_food_page

app_name = 'food_rec'

urlpatterns = [
    path('', show_all_food, name='show_all_food'),
    path('add/', add_food_ajax, name='add_food_ajax'),
    path('json/', show_json, name='show_json'),
    path('rate/<int:id>', rate_food_ajax, name='rate_food_ajax'),
    path('show-food/<int:id>', food_page_by_id, name='food_page_by_id'),
    path('add-food/', add_food_page, name='add_food_page'),
]