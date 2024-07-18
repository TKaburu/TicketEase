from django import forms
from .models import *

class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'attachments']

class TicketMessageForm(forms.ModelForm):
    """
    This form handles logic for messaging in the detail ticket view
    """
    class Meta:
        model = TicketMessage
        fields = ['message']