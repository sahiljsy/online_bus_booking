from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hellow World')


def new(request):
    return HttpResponse('NEW Products')



