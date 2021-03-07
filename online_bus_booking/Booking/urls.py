from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservation),
    path('reservation/transaction', views.transaction),
    path('cancelTicket', views.cancelticket),
    path('cancelTicket/refund', views.refund),
]
