from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import CustomUser


class CustomSignUpForm(SignupForm):
    """
    This form class handles user registration and will be used django allauth
    """
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    bio = forms.CharField(widget=forms.Textarea, label='Bio')
    avatar = forms.ImageField(required=False, label='Avatar')

    def save(self, request):
        """
        Saves all the new field 
        """
        new_user = super(CustomSignUpForm, self).save(request)

        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        # new_user.title = self.cleaned_data['title']
        # new_user.department = self.cleaned_data['department']
        new_user.avatar = self.cleaned_data['avatar']
        new_user.save()
        return new_user
    
class CustomLoginForm(LoginForm):
    """
    This form class handles user login and will be used by django allauth
    """
    remember_me = forms.BooleanField(required=False, label="Remember Me")

    def __init__(self, *args, **kwargs):
        """
        This method initialises a new instace of the CustomLogin form
        """
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['remember_me'].widget.attrs['id'] = 'id_remember'

class UserProfileForm(forms.ModelForm):
    """
    This class defines a form used to update a users profile 
    """
    class Meta:
        model = CustomUser
        fields = '__all__'
