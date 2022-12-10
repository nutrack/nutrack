from django.urls import path
from testimonies.views import *

app_name = 'testimonies'
 
urlpatterns = [
    path('', show_testimonies, name='show_testimonies'),
    path('create-testimonies', create_testimonies, name='create_testimonies'),
    path('create-testimonies-flutter', create_testimonies_flutter, name='create_testimonies_flutter'),
    path('json', testimonies_json, name='testimonies_json'),
    path('add/', create_testimony_ajax, name='create_testimony_ajax')
]