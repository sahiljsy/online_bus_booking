from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus
from django.contrib.auth import logout
from datetime import datetime
# Create your views here.


@login_required(login_url="http://127.0.0.1:8000/login")
def bus(request):
    return render(request, 'info.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def showbus(request):
    bus = Bus.objects.all()
    context= {}
    error = {}
    source = request.POST.get('source', ' ')
    dest = request.POST.get('destination', ' ')
    if source == dest:
        error['place'] = "Source and Destination cannot be same."
        return render(request, 'info.html', error)
    type = request.POST.get('type', ' ')
    date = request.POST.get('date', ' ')
    dt =datetime.strptime(date, '%Y-%m-%d')
    CurrentDate = datetime.now()
    print(CurrentDate)
    if CurrentDate > dt:
        error['date'] = "Invalid Date of journay selected."
        return render(request, 'info.html', error)
    usrnm = request.POST.get('usrnm', ' ')
    context['source'] = source
    context['destination'] = dest
    context['type'] = type
    context['bus'] = bus
    context['date'] = date
    context['usrnm'] = usrnm
    return render(request, 'bus.html', context)





