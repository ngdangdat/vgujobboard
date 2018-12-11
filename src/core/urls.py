from admin.admin import admin_site

from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin_site.urls),
    url(r'^api/', include('api.router')),
    url(r'^(?:.*)/?$', TemplateView.as_view(template_name='index.html'), name='catchall'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
