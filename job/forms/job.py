from django import forms
from django.utils.translation import ugettext_lazy as _
from job.models.job import Job, JobField
from frontsite import widgets
import datetime

class JobForm(forms.ModelForm):
    field = forms.ModelChoiceField(label=('Job Field'), queryset=JobField.objects.all().order_by('name'), required=False)
    other_field = forms.CharField(label=_('Other Field'), required=False)
    title = forms.CharField(label=_('Job Title'), required=True)
    company = forms.CharField(label=_('Company'), required=True)
    description = forms.CharField(label=_('Job Description'), widget=forms.Textarea, required=False)
    requirement = forms.CharField(label=_('Job Requirement'), widget=forms.Textarea, required=True)
    salary = forms.CharField(label=_('Salary'), required=False)
    benefit = forms.CharField(label=_('Benefits'), widget=forms.Textarea, required=False)
    apply_contact = forms.CharField(label=_('Resume Application To'), required=True)
    deadline = forms.DateField(label=_('Deadline'), widget=forms.SelectDateWidget(), required=True)
    question_contact = forms.CharField(label=_('Your Contact'), required=False)
    img_url = forms.URLField(label=_('Image'), widget=widgets.UploadCareUploader(), required=False)

    class Meta:
        model = Job
        exclude = ('is_posted', 'scheduled_time', 'facebook_post_id')

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)


        self.fields['deadline'].widget.attrs['class'] = 'date-input-field'

        self.fields['field'].empty_label = 'Other'
        choices = list(self.fields['field'].choices)
        choices.append(choices.pop(0))
        self.fields['field'].choices = choices
        self.fields['field'].initial = choices[0]

    def clean_field(self):
        field = self.cleaned_data['field']
        other_field = self.data['other_field']
        if not field and not other_field:
            raise forms.ValidationError('Enter your job field.')
        return field

    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        now = datetime.datetime.now()
        if deadline <= now.date():
            raise forms.ValidationError('Please input a future date.')
        return deadline
