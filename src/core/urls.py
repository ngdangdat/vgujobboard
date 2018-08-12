from admin.admin import admin_site
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin_site.urls),
    url(r'^api/', include('api.router')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
