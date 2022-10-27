from django.urls import path,include
from calorycalc.views import calorycalc, test
app_name = 'calorycalc'

urlpatterns = [
    path('', calorycalc, name='calorycalc'),

]