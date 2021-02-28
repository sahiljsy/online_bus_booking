from django.contrib import admin
from .models import Bus


class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_id', 'bus_number', 'type', 'source', 'destination', 'no_of_seats', 'dep_time', 'arr_time', 'pricePerSeat')


admin.site.register(Bus, BusAdmin)
