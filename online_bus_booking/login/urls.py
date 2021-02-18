from django.urls import path
from login.views import login, auth_view, logout, loggedin, invalidlogin, registration, home
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    path('', home),
    path('login/', login),
    path('login/auth/', auth_view),
    path('logout/', logout),
    path('loggedin/', loggedin),
    path('invalidlogin/', invalidlogin),
    path('registration/', registration),
]
