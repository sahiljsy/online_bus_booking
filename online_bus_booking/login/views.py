from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf


# Create your views here.


def login(request):
    return render(request, 'login.html')


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/login/loggedin/')
    else:
        return HttpResponseRedirect('/login/invalidlogin/')


def loggedin(request):
    return HttpResponseRedirect('/bus')


def invalidlogin(request):
    return render(request, 'invalidlogin.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
