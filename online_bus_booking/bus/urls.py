from django.urls import path
from . import views

urlpatterns = [
    path('', views.bus),
    path('new', views.new),
    path('showbus', views.showbus)
]
