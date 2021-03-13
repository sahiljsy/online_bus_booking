from django.urls import path
from login.views import login,  auth_view, loggedin,  registration, home, index, displaydetails, \
    showconfirmation, deleteaccount, accountdeleted, logout_view
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', index),
    path('login/', login),
    path('login/auth/', auth_view),
    path('loggedin/', loggedin),
    path('registration/', registration),
    path('home/', home),
    path('home/updatedetails', displaydetails),
    path('home/confirm', showconfirmation),
    path('home/deleteaccount', deleteaccount),
    path('home/deleted', accountdeleted),
    path('logout/', logout_view)
]
