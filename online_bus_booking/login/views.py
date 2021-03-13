from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import Registration
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Booking.models import Reservation, Transaction


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    context = {'username': username}
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        con = {'invalid_error': "Invalid details of login"}
        return render(request, 'login.html', con)


def loggedin(request):
    return HttpResponseRedirect('/bus')


def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/login/')
    else:
        form = Registration()
    return render(request, 'registration.html', {'form': form})


@login_required(login_url="http://127.0.0.1:8000/login")
def displaydetails(request):
    if request.method == 'POST':
        usrnm = request.POST.get('usernm', ' ')
        eml = request.POST.get('email', ' ')
        firstnm = request.POST.get('first', ' ')
        lastnm = request.POST.get('last', ' ')
        user = request.user.id
        User.objects.filter(id=user).update(username=usrnm, email=eml, first_name=firstnm, last_name=lastnm)
        return render(request, 'confirmupdate.html')
    else:
        return render(request, 'displaydetails.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def showconfirmation(request):
    usrnm = request.POST.get('usernm', ' ')
    eml = request.POST.get('email', ' ')
    firstnm = request.POST.get('first', ' ')
    lastnm = request.POST.get('last', ' ')
    user = request.user.id
    t = User.objects.filter(id=user).update(username=usrnm, email=eml, first_name=firstnm, last_name=lastnm)
    return render(request, 'confirmupdate.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def deleteaccount(request):
    return render(request, 'deleteaccount.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def accountdeleted(request):
    user = request.user.id
    User.objects.filter(id=user).delete()
    return redirect('http://127.0.0.1:8000/login/')


def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000')




