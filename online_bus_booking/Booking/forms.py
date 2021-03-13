from django import forms
from .models import PromoCode
from bus.models import Bus

CHOICES= [
    ('Debit Card', 'Debit Card'),
    ('Credit card', 'Credit card'),
    ('Net Banking', 'Net Banking'),
    ('UPI', 'UPI'),
    ]


class ReserveTickets(forms.Form):
    def __init__(self, *args, **kwargs):
        self._bid = kwargs.pop('bus_id', None)
        super().__init__(*args, **kwargs)
    numberofseats = forms.IntegerField(required=True,help_text="Enter the number of tickets.")
    payMeth = forms.CharField(required=False,widget=forms.Select(choices=CHOICES))
    promocode = forms.CharField(required=False)
    def clean_numberofseats(self):
        global numofseats
        numofseats = self.cleaned_data.get('numberofseats')
        available_seats = Bus.objects.get(bus_id = self._bid).__getattribute__('available_seat')
        if numofseats > available_seats:
            raise forms.ValidationError("Enough Seats are not available.")
        if numofseats <= 0:
            raise forms.ValidationError("Invalid number of seats given.")
        return numofseats 
    def clean_promocode(self):
        data = self.cleaned_data.get('promocode')
        table = PromoCode.objects.filter(code=data).exists()
        if table == False:
            return None
        else:
            obj = PromoCode.objects.get(code=data)
            nooftickets = obj.__getattribute__('numberoftickets')
            if nooftickets < numofseats:
                return data
            else:
                raise forms.ValidationError("This promocode is not applicable here.Please try another code.")

