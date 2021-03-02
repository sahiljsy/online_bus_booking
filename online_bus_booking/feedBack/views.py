from django.shortcuts import render
from .models import FeedBack

# Create your views here.

def giveFeedBack(request):
    return render(request, 'feedBack.html')

def viewFeedBack(request):
    feedback = FeedBack.objects.all()
    return render(request, 'viewFeedBack.html', {'feedback': feedback})

def greet(request):
    semail = request.POST.get('email', '')
    srating = request.POST.get('ratings', '')
    ssugg = request.POST.get('suggestions', '')
    s = FeedBack(email = semail, ratings=srating, suggestions=ssugg)
    s.save()
    return render(request, 'greetings.html')


def aboutUs(request):
    return render(request, 'about.html')
