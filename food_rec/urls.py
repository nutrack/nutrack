from django.urls import path
from food_rec.views import show_all_food, show_food_food, show_user_food, add_food_ajax, show_json, food_page_by_id, add_food_page, show_food_drink, sort_food, add_food_flutter

app_name = 'food_rec'

urlpatterns = [
    path('', show_all_food, name='show_all_food'),
    path('', show_food_food, name='show_food_food'),
    path('', show_food_drink, name='show_food_drink'),
    path('my-food/', show_user_food, name='show_user_food'),
    path('add/', add_food_ajax, name='add_food_ajax'),
    path('json/', show_json, name='show_json'),
    path('show-food/<int:id>', food_page_by_id, name='food_page_by_id'),
    path('add-food/', add_food_page, name='add_food_page'),
    
    # flutter
    path('add-food-flutter/', add_food_flutter, name='add_food_flutter')
]