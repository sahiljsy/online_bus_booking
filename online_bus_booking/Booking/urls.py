from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('reservation/transaction', views.transaction),
]
