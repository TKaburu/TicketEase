from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from .models import Ticket

# home view
def home(request):
    """
    Logic for the home view
    """
    tickets = Ticket.objects.all()

    context = {'tickets': tickets}
    return render(request, 'tickets/home.html', context)

def ticketsView(request):
    """
    Logic for the tickets page
    """
    status = request.GET.get('status')  # Get the status from the query parameters
    if status:
        tickets = Ticket.objects.filter(status=status)
    else:
        tickets = Ticket.objects.all()
    
    # Get the counts for each status
    open_count = Ticket.objects.filter(status='open').count()
    pending_count = Ticket.objects.filter(status='pending').count()
    closed_count = Ticket.objects.filter(status='closed').count()
    all_count = Ticket.objects.count()

    context = {
        'tickets': tickets,
        'open_count': open_count,
        'pending_count': pending_count,
        'closed_count': closed_count,
        'all_count': all_count,
        'selected_status': status,
    }
    return render(request, 'tickets/tickets-view.html', context)