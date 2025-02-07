from django import forms
from .models import Complaint, PaymentRecord

class PaymentRecordForm(forms.ModelForm):
    class Meta:
        model = PaymentRecord
        fields = ['name', 'room_no', 'contact', 'receipt']
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'contact', 'room_number', 'message', 'image', 'video']
