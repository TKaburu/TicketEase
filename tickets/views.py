from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *

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
    Has search functionality enabling user to search a
    ticket by title, description status, who ticket is assigned_to
    and created_by
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

    tickets = tickets.order_by('-status', '-created_on')
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

@login_required(login_url=('account_login'))
def ticketDetails(request, slug):
    """
    logic for the ticket detail page
    Users can send messages within this view
    Args:
        slug: the ticket slug
    """
    ticket = Ticket.objects.get(slug=slug)
    msg = ticket.messages.all().order_by('sent_on')  # msg = messages 

    if request.method == 'POST':
        # create the new message
        ticket_message = TicketMessage.objects.create(
            sender=request.user,
            ticket=ticket,
            message=request.POST.get('message')
        )
    context = {
        'ticket': ticket,
        'msg': msg
    }
    return render(request, 'tickets/ticket-details.html', context)

@login_required(login_url=('account_login'))
def deleteMessage(request, msg_id):
    """
    Logic for deleting a message within the detailed view
    Args:
        msg_id: The id of the messahge to be deleted
    """
    message = get_object_or_404(TicketMessage, pk=msg_id)
    ticket_slug = message.ticket.slug

    if request.method == 'POST':
        if request.user == message.sender:
            message.delete()
            messages.success(request, f'The message has been deleted')
        else:
            messages.warning(request, f'You do not have permission to delete this message!')
            return redirect('ticket-details', slug=ticket_slug)
        
    
    return render(request, 'tickets/delete.html', {'obj': message})