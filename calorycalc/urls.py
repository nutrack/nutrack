from django.urls import path,include
from calorycalc.views import add_calory, calorycalc, history, show_calory_json, show_history_by_id_json, test
app_name = 'calorycalc'

urlpatterns = [
    path('', calorycalc, name='calorycalc'),
    path("json/", show_calory_json, name="show_calory_json"),
    path("add_calory/", add_calory, name="add_calory"),
    path("history/<int:id>",history,name="history"),
    path("history_json/<int:id>",show_history_by_id_json,name="show_history_by_id_json")

]