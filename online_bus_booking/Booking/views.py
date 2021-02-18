from django.shortcuts import render
from django.http import HttpResponse
from .models import PromoCode, Reservation, Transaction
# Create your views here.


def index(request):
    return render(request, 'booking.html')


def reservation(request):
    return render(request, 'reservation.html')


def transaction(request):
    return render(request, 'transaction.html')
