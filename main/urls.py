from django.urls import path
from main.views import home, register, login_user, logout_user, show_calory_info, calorycalc_json, choose_user

app_name = 'main'

urlpatterns = [
    path('', choose_user, name="choose"),
    path('home/', home, name='home'),
    path('calc/', show_calory_info, name='caloryInfo'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', calorycalc_json, name='calorycalc_json'),
]