from django.urls import path
from testimonies.views import show_testimonies

app_name = 'testimonies'
 
urlpatterns = [
    path('', show_testimonies, name='show_testimonies'),
]