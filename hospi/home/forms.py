from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'p_name':"Patiant Name", 
            "p_phone":"Phone Number",
            "p_mail":"Email",
            "doc_name":"Select Docter",
            "booking_date":"Slot Date",
        }