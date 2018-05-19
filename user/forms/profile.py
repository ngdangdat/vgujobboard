from django import forms
from user.models import Profile

class ProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    exclude = ['user']

  def save(self, commit=True, *args, **kwargs):
    if not self.instance.pk and 'user' in kwargs:
      self.instance.user = kwargs['user']
    if commit:
      super(ProfileForm, self).save()
    return self.instance
