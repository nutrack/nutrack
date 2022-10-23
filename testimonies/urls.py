from django.urls import path
from .views import *

app_name = 'testimonies'

urlpatterns = [
    path('json/',testimonies_json,name='testimonies_json'),
    path('',show_testimonies,name='show_testimonies'),
    path('add-testimony',create_testimony,name='create_testimony'),
]