from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tickets/', ticketsView, name='tickets-view'),
    path('tickets/<slug:slug>/', ticketDetails, name='ticket-details'),
    path('create-ticket/', createTicket, name='create-ticket'),
    path('tickets/<slug:slug>/accept/', acceptTicket, name='accept-ticket'),
    path('tickets/<slug:slug>/close/', closeTicket, name='close-ticket'),
    path('engineer/<str:username>/dashboard', engineerDashboard, name='engineer-dashboard'),
    path('client/<str:username>/dashboard', clientDashboard, name='client-dashboard'),
    path('delete-message/<int:msg_id>/', deleteMessage, name='delete-message'),
]