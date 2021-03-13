from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PromoCode, Reservation, Transaction
from .forms import ReserveTickets
from bus.models import Bus
from django.contrib.auth import logout


# Create your views here.

@login_required(login_url="http://127.0.0.1:8000/login")
def index(request):
    context = {}
    id = request.POST.get('id', None)
    dates = request.POST.get('dates', None)
    username = request.POST.get('username')
    price = request.POST.get('price', 0)
    context['id'] = id
    context['dates'] = dates
    context['username'] = username
    context['price'] = price
    form = ReserveTickets()
    if request.method == 'POST':
        form = ReserveTickets(request.POST)
        if form.is_valid():
            print('Form Validated.')
            numberofseats = form.cleaned_data.get('numberofseats')
            payMeth = form.cleaned_data.get('payMeth')
            promocode = form.cleaned_data.get('promocode')
            context['promocode'] = promocode
            context['numberofseats'] = numberofseats
            context['payMeth'] = payMeth
            global getdictionary

            def getdictionary():
                return context

            context['form'] = form
            return redirect(transaction)
        else:
            print(form.errors)
    context['form'] = form
    return render(request, 'reservation.html', context)


@login_required(login_url="http://127.0.0.1:8000/login")
def transaction(request):
    context = getdictionary()
    number_of_tickets = int(context['numberofseats'])
    id = context['id']
    # id = request.POST.get('id', '')
    dateofjourney = context['dates']
    usernm = request.user.username
    price = int(context['price'])
    paymentMeth = context['payMeth']
    promocode = context['promocode']
    obj = PromoCode.objects.get(code=promocode)
    disc = obj.__getattribute__('discount')
    # print(id,number_of_tickets,price,promocode,obj,disc)
    amnt = price * number_of_tickets * (1 - disc)
    s = Reservation(numberOfTicket=number_of_tickets, dateOfJourney=dateofjourney, bus_id=id, username=usernm)
    s.save()
    t = Transaction(username=usernm, date=dateofjourney, amount=amnt, payment_method=paymentMeth, refund_amount=0)
    t.save()
    context['ticket_no'] = s.id
    context['transaction_id'] = t.id
    context['amount'] = amnt
    b = Bus.objects.get(bus_id=id)
    context['bus_number'] = b.bus_number
    ava_seat = b.available_seat
    ava_seat = ava_seat - number_of_tickets
    Bus.objects.filter(bus_id=id).update(available_seat=ava_seat)
    return render(request, 'transaction.html', context)


@login_required(login_url="http://127.0.0.1:8000/login")
def cancelticket(request):
    return render(request, 'cancelTicket.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def viewticket(request):
    return render(request, 'viewTicket.html')


@login_required(login_url="http://127.0.0.1:8000/login")
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
            rf = t.amount * .9
            ct = Transaction(username=t.username, date=t.date, amount=t.amount, payment_method=t.payment_method,
                             refund_amount=rf)
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


@login_required(login_url="http://127.0.0.1:8000/login")
def downloadticket(request):
    error = {}
    details = {}
    ticketid = int(request.POST.get('ticketid', ''))
    transactionid = int(request.POST.get('transactionid', ''))
    try:
        r = Reservation.objects.get(id=ticketid)
        t = Transaction.objects.get(id=transactionid)
        busid = r.bus_id
        b = Bus.objects.get(bus_id=busid)
        details['bus_number'] = b.bus_number
        details['ticket_no'] = ticketid
        details['transaction_id'] = transactionid
        details['numberofseats'] = r.numberOfTicket
        details['dates'] = r.dateOfJourney
        details['amount'] = t.amount
        return render(request, 'downloadticket.html', details)
    except Reservation.DoesNotExist:
        error['ticket_error'] = "Invalid Ticket details"
        return render(request, 'viewTicket.html', error)
    except Transaction.DoesNotExist:
        error['pay_error'] = "Invalid Transaction details"
        return render(request, 'viewTicket.html', error)


@login_required(login_url="http://127.0.0.1:8000/login")
def userTransactions(request):
    context = {}
    username = request.user.username
    user_detail = {'username': username}
    reservation = Reservation.objects.all()
    trans = Transaction.objects.all()
    context['reservation'] = reservation
    context['username'] = username
    context['transaction'] = trans

    return render(request, 'usertransaction.html', context)
