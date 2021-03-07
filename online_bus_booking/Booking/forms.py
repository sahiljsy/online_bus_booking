from django import forms
from .models import Reservation, Transaction


class Reservation_Valid(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


class Transaction_Valid(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
