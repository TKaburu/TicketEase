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
    tickets = Ticket.objects.all()
    status = request.GET.get('status')  # to filter by status
    query = request.GET.get('q')  # search parameter
    if status:
        tickets = Ticket.objects.filter(status=status)

    elif query:
        tickets = tickets.filter(
            Q(title__icontains=query) |  # Case-insensitive search in title
            Q(description__icontains=query) |
            Q(status__icontains=query) |
            Q(created_by__username__icontains=query) |
            Q(assigned_to__username__icontains=query)
        )

    else:
        tickets = Ticket.objects.all()
    # Get the counts for each status
    all_count = Ticket.objects.count()
    open_count = Ticket.objects.filter(status='open').count()
    assigned_count = Ticket.objects.filter(status='assigned').count()
    closed_count = Ticket.objects.filter(status='closed').count()

    context = {
        'tickets': tickets,
        'open_count': open_count,
        'assigned_count': assigned_count,
        'closed_count': closed_count,
        'all_count': all_count,
        'selected_status': status,
    }
    return render(request, 'tickets/tickets-view.html', context)

