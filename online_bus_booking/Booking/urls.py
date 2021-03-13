from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('reservation/transaction', views.transaction),
    path('cancelTicket', views.cancelticket),
    path('cancelTicket/refund', views.refund),
    path('viewTicket', views.viewticket),
    path('viewTicket/download', views.downloadticket),
    path('usertransaction/', views.userTransactions),
]
