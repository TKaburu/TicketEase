from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class TicketEaseAdapter(DefaultAccountAdapter):
    """
    This class changes the default behaviour of the application such as
    changing the redirect login url
    """

    def get_login_redirect_url(self, request):
        """
        gets the new login url path that redirects a user
        to the home page after login in.
        If usert is client they are redirected to client-dashboard
        if user is engineer they are redirected to engineer dashboard
        else redirect home
        """
        
        user = request.user

        if user.user_type == 'client':
            return reverse('client-dashboard', kwargs={'username': user.username})
        elif user.user_type == 'engineer':
            return reverse('tickets-view')
        else:
            return reverse('home') 