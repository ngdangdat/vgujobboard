from django.contrib.admin import AdminSite as OrgAdminSite
from django.contrib import admin
from django.views.decorators.cache import never_cache
from django.template.response import TemplateResponse

class AdminSite(OrgAdminSite):
    site_title = 'VGU Alumni CMS'

    @never_cache
    def index(self, request, extra_context=None):
        app_list = self.get_app_list(request)
        context = dict(
            self.each_context(request),
            title=self.index_title,
            app_list=app_list,
        )
        context.update(extra_context or {})
        request.current_app = self.name
        return TemplateResponse(request, self.index_template or 'admin/index.html', context)

admin_site = AdminSite()
# admin.site = admin_site

from job.models import *
from .job import JobAdmin
from .job import JobFieldAdmin

# Job

admin_site.register(Job, JobAdmin)
admin_site.register(JobField, JobFieldAdmin)
