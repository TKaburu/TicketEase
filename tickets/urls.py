from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tickets/', ticketsView, name='tickets-view'),
    path('tickets/<slug:slug>/', ticketDetails, name='ticket-details'),
    path('delete-message/<int:msg_id>/', deleteMessage, name='delete-message'),
]