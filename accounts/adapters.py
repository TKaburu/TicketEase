from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import resolve_url

class TicketEaseAdapter(DefaultAccountAdapter):
    """
    This class changes the default behaviour of the application such as
    changing the redirect login url
    """

    def get_login_redirect_url(self, request):
        """
        gets the new login url path that redirects a user
        to the home page after login in
        """
        url_path = "/"
        return url_path