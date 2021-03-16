from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus
from django.contrib.auth import logout
# Create your views here.


@login_required(login_url="http://127.0.0.1:8000/login")
def bus(request):
    return render(request, 'info.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def showbus(request):
    bus = Bus.objects.all()
    context= {}
    source = request.POST.get('source',' ')
    dest = request.POST.get('destination',' ')
    type = request.POST.get('type',' ')
    date = request.POST.get('date',' ')
    usrnm = request.POST.get('usrnm',' ')
    context['source'] = source
    context['destination'] = dest
    context['type'] = type
    context['bus'] = bus
    context['date'] = date
    context['usrnm'] = usrnm
    return render(request, 'bus.html', context)





