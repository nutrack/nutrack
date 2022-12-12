from django.urls import path,include
from calorycalc.views import add_calory, calorycalc, histories, history, show_calory_json, show_history_by_id_json, test, add_calory_flutter,show_calory_json_flutter
app_name = 'calorycalc'

urlpatterns = [
    path('', calorycalc, name='calorycalc'),
    path("json/", show_calory_json, name="show_calory_json"),
    path("json_flutter/", show_calory_json_flutter, name="show_calory_json_flutter"),
    path("add_calory/", add_calory, name="add_calory"),
    path('add_calory_flutter/', add_calory_flutter, name='add_calory_flutter'),
    path("history/<int:id>",history,name="history"),
    path("history_json/<int:id>",show_history_by_id_json,name="show_history_by_id_json"),
    path("histories/",histories,name="histories")

]