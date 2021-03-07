from django.shortcuts import render
from django.http import HttpResponse
from .models import PromoCode, Reservation, Transaction
from bus.models import Bus
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


def cancelticket(request):
    return render(request, 'cancelTicket.html')


def refund(request):
    error = {}
    ticketid = int(request.POST.get('ticketid', ''))
    transactionid = int(request.POST.get('transactionid', ''))
    noofseat = int(request.POST.get('noofseats', ''))
    try:
        r = Reservation.objects.get(id=ticketid)
        t = Transaction.objects.get(id=transactionid)
        if noofseat > 0 and noofseat == r.numberOfTicket:
            busid = r.bus_id
            b = Bus.objects.get(bus_id=busid)
            avail_seat = b.available_seat + noofseat
            Bus.objects.filter(bus_id=busid).update(available_seat=avail_seat)
            rf = t.amount*.9
            ct = Transaction(username=t.username, date=t.date, amount=t.amount, payment_method=t.payment_method, refund_amount=rf)
            ct.save()
            r.delete()
            t.delete()
            return render(request, 'refund.html')
        else:
            error['no_error'] = "Invalid Number of seat details"
            return render(request, 'cancelTicket.html', error)
    except Reservation.DoesNotExist:
        error['ticket_error'] = "Invalid Ticket details"
        return render(request, 'cancelTicket.html', error)
    except Transaction.DoesNotExist:
        error['pay_error'] = "Invalid Transaction details"
        return render(request, 'cancelTicket.html', error)



