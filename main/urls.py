from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', choose_user, name="choose"), #choosing unauth user or auth user
    path('home/', home, name='home'), #routing for unauth user
    path('calc/', show_calory_info, name='caloryInfo'), #routing for auth user
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', calorycalc_json, name='calorycalc_json'),
    path('about/', about, name='about'),
    path('register-flutter/', register_flutter, name='register_flutter'),
    path('login-flutter/', login_flutter, name='login_flutter'),
    path('logout-flutter/', logout_flutter, name='logout_flutter'),
]