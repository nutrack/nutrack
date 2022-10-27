from django.shortcuts import render
from calorycalc.models import caloryInfo
from django.contrib.auth.decorators import login_required
# Create your views here.

def test(request):
    return render(request,"test.html")


#@login_required(login_url='/login/')
def calorycalc(request):
    data=caloryInfo.objects.all()
    context = {
    'calory' : data,
    }
    return render(request, "calorycalc.html", context)