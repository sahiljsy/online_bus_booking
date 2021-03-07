from django.contrib import admin
from .models import PromoCode, Reservation, Transaction


class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'numberOfTicket', 'dateOfJourney', 'bus_id')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date', 'amount', 'payment_method', 'refund_amount')


admin.site.register(PromoCode, PromoCodeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Transaction, TransactionAdmin)
