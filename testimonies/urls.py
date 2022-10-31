from django.urls import path
from testimonies.views import *

app_name = 'testimonies'
 
urlpatterns = [
    path('', show_testimonies, name='show_testimonies'),
    path('create-testimonies', create_testimonies, name='create_testimonies'),
]