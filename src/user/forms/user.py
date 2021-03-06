from django import forms
from user.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.forms import \
  (
    UserCreationForm as BaseUserCreationForm,
    PasswordResetForm as BasePasswordResetForm
  )

from django.utils.translation import gettext_lazy as _

class RegisterForm(BaseUserCreationForm):

  error_messages = {
    'password_mismatch': _("The two password fields didn't match.")
  }
  email = forms.CharField(
    label=_("Email"),
    required=True,
  )
  first_name = forms.CharField(
    label=_("First Name"),
    required=True,
  )
  last_name = forms.CharField(
    label=_("Last Name"),
    required=True,
  )

  class Meta:
    model = User
    fields = ('email', 'first_name', 'last_name' ,'password1', 'password2',)

  def save(self, commit=True):
    user = super().save(commit=False)
    user.is_active = False
    if commit:
      user.save()
    return user

class PasswordResetForm(BasePasswordResetForm):
  """Override password reset form here"""
  pass