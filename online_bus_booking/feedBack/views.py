from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import FeedBack
from django.contrib.auth import logout
from django.http import FileResponse, Http404


# Create your views here.
@login_required(login_url="http://127.0.0.1:8000/login")
def giveFeedBack(request):
    return render(request, 'feedBack.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def viewFeedBack(request):
    feedback = FeedBack.objects.all()
    return render(request, 'viewFeedBack.html', {'feedback': feedback})


@login_required(login_url="http://127.0.0.1:8000/login")
def greet(request):
    error = {}
    semail = request.POST.get('email', '')
    rating = request.POST.get('ratings')
    if rating == '':
        error['ratings'] = "No Ratings given."
        return render(request, 'feedBack.html', error)
    try:
        srating = int(rating)
    except:
        error['ratings'] = "Invalid Ratings given.It should be from 1 to 5"
        return render(request, 'feedBack.html', error)
    ssugg = request.POST.get('suggestions', '')
    if srating < 0 or srating > 5:
        error['ratings'] = "Invalid Ratings given."
        return render(request, 'feedBack.html', error)
    else:
        s = FeedBack(email=semail, ratings=srating, suggestions=ssugg)
        s.save()
        return render(request, 'greetings.html')


def aboutUs(request):
    return render(request, 'about.html')


@login_required(login_url="http://127.0.0.1:8000/login")
def help_(request):
    try:
        return FileResponse(open('dfd.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
