from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets={
            'booking_date':DateInput(),
        }

        labels ={
            "p_name":"Patiant name ",
            'p_phone':"Patiant Phone ",
            "p_email":"Patiant Email ",
            "doc_name":"Doctor Name ",
            "booking_date":"Booking Date ",
        }