from django.forms import widgets
from django.template.loader import render_to_string

class UploadCareUploader(widgets.URLInput):

    template_name = 'components/uploadcare.html'

    class Media(object):
        js = ('js/uploadcare.js',)

    def render(self, name, value, attrs=None, choices=()):
        return render_to_string(
            template_name=self.template_name,
            context=dict(
                name=name,
                value=value,
                media=self.media
            )
        )