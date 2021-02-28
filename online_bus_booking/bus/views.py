from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus
# Create your views here.


def bus(request):
    return render(request, 'info.html')


def new(request):
    return HttpResponse("welcome to new page!!")

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





