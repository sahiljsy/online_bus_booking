from django.urls import path
from feedBack.views import giveFeedBack,viewFeedBack
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', giveFeedBack),
    path('ViewFeedBack/', viewFeedBack),
]