from django.urls import path
from . import views

urlpatterns = [
    path('', views.bus),
    path('showbus', views.showbus)
]
