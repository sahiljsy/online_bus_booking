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
    semail = request.POST.get('email', '')
    srating = request.POST.get('ratings', '')
    ssugg = request.POST.get('suggestions', '')
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
