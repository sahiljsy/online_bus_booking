from django import forms
from .models import PromoCode
from bus.models import Bus

CHOICES = [
    ('Debit Card', 'Debit Card'),
    ('Credit card', 'Credit card'),
    ('Net Banking', 'Net Banking'),
    ('UPI', 'UPI'),
]


class ReserveTickets(forms.Form):
    numberofseats = forms.IntegerField(required=True, help_text="Enter the number of tickets.")
    payMeth = forms.CharField(required=False, widget=forms.Select(choices=CHOICES))
    promocode = forms.CharField(required=False, min_length=6)

    def clean_numberofseats(self):
        global numofseats
        numofseats = self.cleaned_data.get('numberofseats')
        if numofseats < 5:
            raise forms.ValidationError("Available seats are only 5.")
        return numofseats

    def clean_promocode(self):
        data = self.cleaned_data.get('promocode')
        table = PromoCode.objects.filter(code=data).exists()
        if table == False:
            raise forms.ValidationError("Promocode is not applicable.")
        else:
            obj = PromoCode.objects.get(code=data)
            nooftickets = obj.__getattribute__('numberoftickets')
            if nooftickets < numofseats:
                return data
            else:
                raise forms.ValidationError("This promocode is not applicable here.Please try another code.")
