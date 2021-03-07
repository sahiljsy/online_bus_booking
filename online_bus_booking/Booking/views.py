from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PromoCode, Reservation, Transaction
from .forms import ReserveTickets
# Create your views here.


def index(request):
    context= {}
    id = request.POST.get('id',None)
    dates = request.POST.get('dates',None)
    username = request.POST.get('username')
    price = request.POST.get('price',0)
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
            context['promocode']=promocode
            context['numberofseats']=numberofseats
            context['payMeth']=payMeth
            global getdictionary
            def getdictionary():
                return context
            context['form'] = form
            return redirect(transaction)
        else:
            print(form.errors)
    context['form'] = form
    return render(request, 'reservation.html',context)


def transaction(request):
    context = getdictionary()
    number_of_tickets = int(context['numberofseats'])
    id = context['id']
    #id = request.POST.get('id', '')
    dateofjourney = context['dates']
    usernm = context['username']
    price =int(context['price'])
    paymentMeth=context['payMeth']
    promocode = context['promocode']
    obj = PromoCode.objects.get(code=promocode)
    disc = obj.__getattribute__('discount')
    # print(id,number_of_tickets,price,promocode,obj,disc)
    amnt = price*number_of_tickets*(1-disc)
    s = Reservation(numberOfTicket = number_of_tickets, dateOfJourney=dateofjourney, bus_id=id)
    s.save()
    t = Transaction(username=usernm,date=dateofjourney,amount=amnt,payment_method=paymentMeth,refund_amount=0)
    t.save()
    return render(request, 'transaction.html')
