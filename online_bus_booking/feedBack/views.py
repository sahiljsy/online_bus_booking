from django.shortcuts import render
from .models import FeedBack

# Create your views here.

def giveFeedBack(request):
    return render(request, 'feedBack.html')

def viewFeedBack(request):
    feedback = FeedBack.objects.all()
    return render(request, 'viewFeedBack.html', {'feedback': feedback})