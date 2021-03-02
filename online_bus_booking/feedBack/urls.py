from django.urls import path
from feedBack.views import giveFeedBack, viewFeedBack, greet, aboutUs
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', giveFeedBack),
    path('ViewFeedBack/', viewFeedBack),
    path('Greetings/', greet),
    path('about/', aboutUs)
]