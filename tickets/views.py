from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage  # for sending emails
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
import datetime  # for the accepted time for the ticket

# home view
def home(request):
    """
    Logic for the home view
    """
    tickets = Ticket.objects.all()

    context = {'tickets': tickets}
    return render(request, 'tickets/home.html', context)

def contact(request):
    """
    logic for the contact page
    """

    if request.method == 'POST':
        sender_name = request.POST.get('sender-name', '')
        sender_email = request.POST.get('sender-email', '')
        message_title = request.POST.get('message-title', '')
        message_body = request.POST.get('message-body', '')

        send_mail (
            message_title,
            message_body,
            sender_email,
            ['ticketwithease@gmail.com'],
        )
        messages.success(request, f'The message has been sent. We will get back to you\
                         as soon as possible!')
        return redirect('contact')
    
    return render(request, 'tickets/contact.html')

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
    active_count = Ticket.objects.filter(status='active').count()
    closed_count = Ticket.objects.filter(status='closed').count()

    context = {
        'tickets': tickets,
        'open_count': open_count,
        'active_count': active_count,
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
        return redirect('ticket-details', slug=slug)

    context = {
        'ticket': ticket,
        'msg': msg,
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

# <==================== Clientss views ====================>
@login_required(login_url=('account_login'))
def clientDashboard(request, username):
    """
    logic for a dashboard that shows all the tickets a client has
    Creates on
    Args:
        username: the request user who is a client
    """
    current_client = get_object_or_404(CustomUser, username=username)
    tickets = Ticket.objects.filter(created_by=current_client)
    status = request.GET.get('status')
    query = request.GET.get('Q')

    if status:
        tickets = Ticket.objects.filter(status=status)

    elif query:
        tickets = tickets.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(status__icontains=query) |
            Q(assigned_to__username__icontains=query)
        )

    tickets = tickets.order_by('-status', '-created_on')
    # Get the relative counts for the dashboard
    all_count = tickets.count()
    active_count = tickets.filter(status='active').count()
    closed_count = tickets.filter(status='closed').count()

    context = {
        'tickets': tickets,
        'all_count': all_count,
        'active_count': active_count,
        'closed_count': closed_count,
        }

    return render(request, 'tickets/client-dashboard.html', context)

@login_required(login_url=('account_login'))
def createTicket(request):
    """
    Logic for creating a new ticket
    """
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect('tickets-view')
    else:
        form = NewTicketForm()
    return render(request, 'tickets/create-ticket.html', {'form': form})


# <==================== Engineers views ====================>

@login_required(login_url=('account_login'))
def acceptTicket(request, slug):
    """
    logic for engineer accepting a ticket
    Args:
        slug: the slug of the ticket
    """
    ticket = get_object_or_404(Ticket, slug=slug)

    if request.user.user_type == 'engineer':
    
        ticket.status = 'active'
        ticket.assigned_to = request.user
        ticket.accepted_on = datetime.datetime.now()
        ticket.save()
    # else:
    #     messages.warning(request, f'Only engineers can accept a ticket!')
    #     return redirect('ticket_details', slug=slug)

    return redirect('tickets-detail')

@login_required(login_url=('account_login'))
def closeTicket(request, slug):
    """
    logic for closing a ticket by the accepted engineer when it is resolved
    Args:
        slug: the ticket slug
    """
    ticket = get_object_or_404(Ticket, slug=slug)

    if request.user == ticket.assigned_to:
        ticket.status = 'closed'
        ticket.closed_on = datetime.datetime.now()
        ticket.save()

    return redirect('tickets-view')

@login_required(login_url=('account_login'))
def engineerDashboard(request, username):
    """
    logic for a dashboard that shows all the tickets an engineer has
    worked on
    Args:
        user: the request user who is an engineer
    """
    current_engineer = get_object_or_404(CustomUser, username=username)
    tickets = Ticket.objects.filter(assigned_to=current_engineer)
    status = request.GET.get('status')
    query = request.GET.get('Q')

    if status:
        tickets = Ticket.objects.filter(status=status)

    elif query:
        tickets = tickets.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(status__icontains=query) |
            Q(created_by__username__icontains=query)
        )

    tickets = tickets.order_by('-status', '-created_on')
    # Get the relative counts for the dashboard
    all_count = tickets.count()
    active_count = tickets.filter(status='active').count()
    closed_count = tickets.filter(status='closed').count()

    context = {
        'tickets': tickets,
        'all_count': all_count,
        'active_count': active_count,
        'closed_count': closed_count,
        }

    return render(request, 'tickets/engineer-dashboard.html', context)
