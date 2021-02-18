from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus
# Create your views here.


def bus(request):
    bus = Bus.objects.all()
    return render(request, 'bus.html', {'bus': bus})


def new(request):
    return HttpResponse("welcome to new page!!")





