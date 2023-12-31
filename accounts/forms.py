# Custom User Auth Form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class UserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password field with admin's password hash display field."""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')