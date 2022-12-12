from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from calorycalc.forms import TaskForm  
# Create your views here.
from calorycalc.models import caloryInfo  



def test(request):
    return render(request,"test.html")


@login_required(login_url='/login/')
def calorycalc(request):
    data=caloryInfo.objects.filter(user=request.user)
    if(len(list(data))!=0):
        if(list(data)[0].date.day!=datetime.datetime.now().day):
            data=caloryInfo.objects.filter(user=request.user).delete()
            
    
    context = {
    'date':datetime.datetime.now(),
    'calory' : data,
    }
    return render(request, "calorycalc.html", context)


def show_calory_json(request):
    date = datetime.date.today()
    caloryInfo.objects.filter(date__lt=date,user=request.user).delete()
    tasks = list(caloryInfo.objects.filter(user=request.user).values())
    return JsonResponse(tasks, safe=False)

def show_calory_json_flutter(request):
    date = datetime.date.today()
    caloryInfo.objects.filter(date__lt=date).delete()
    data = caloryInfo.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")




@csrf_exempt
def add_calory(request):
    form = TaskForm(request.POST)
    form.instance.user = request.user
    if form.is_valid():
        form.save()
        return JsonResponse({'calory':form.instance.calory,"date": form.instance.date,"id":form.instance.pk})
    return redirect("calorycalc:calorycalc")

    
@csrf_exempt
def add_calory_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = datetime.datetime.now()
        calory = data['calory']
        user = request.user

        data = caloryInfo.objects.create(
            user=user,
            date=date,
            calory=calory,
        )

        data.save()

        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'failed'}, status=401)






@login_required(login_url='/login/')
def history(request,id):
    data=caloryInfo.objects.filter(user=request.user,pk=id)
    if(len(list(data))!=0):
        if(list(data)[0].date.day!=datetime.datetime.now().day):
            data=caloryInfo.objects.filter(user=request.user).delete()
    context = {
    'data' : data,
    }
    return render(request, "historycalc.html", context)

def show_history_by_id_json(request,id):
    datas=list(caloryInfo.objects.filter(pk=id).values())
    return JsonResponse(datas, safe=False)



@login_required(login_url='/login/')
def histories(request):
    data=caloryInfo.objects.filter(user=request.user)
    if(len(list(data))!=0):
        if(list(data)[0].date.day!=datetime.datetime.now().day):
            data=caloryInfo.objects.filter(user=request.user).delete()
    context = {
    'data' : data,
    }
    return render(request, "history.html", context)
