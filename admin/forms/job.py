from django import forms

class JobFieldForm(forms.ModelForm):

    class Meta:
        exclude = ['slug']
