from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello World of Python")


def new(request):
    return HttpResponse("welcome to new page!!")




