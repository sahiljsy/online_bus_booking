from django.shortcuts import render
from django.http import HttpResponse
from .models import PromoCode, Reservation, Transaction
# Create your views here.


def index(request):
    context= {}
    id = request.POST.get('id',' ')
    dates = request.POST.get('dates',' ')
    username = request.POST.get('username',' ')
    price = request.POST.get('price',' ')
    context['id'] = id
    context['dates'] = dates
    context['username'] = username
    context['price'] = price
    return render(request, 'reservation.html',context)



def transaction(request):
    number_of_tickets = int(request.POST.get('numberofseats', ''))
    id = request.POST.get('id', '')
    dateofjourney = request.POST.get('dates', '')
    usernm = request.POST.get('username', '')
    price = int((request.POST.get('price', '')))
    paymentMeth=request.POST.get('payMeth','')
    amnt = price*number_of_tickets
    s = Reservation(numberOfTicket = number_of_tickets, dateOfJourney=dateofjourney, bus_id=id)
    s.save()
    t = Transaction(username=usernm,date=dateofjourney,amount=amnt,payment_method=paymentMeth,refund_amount=0)
    t.save()
    return render(request, 'transaction.html')
