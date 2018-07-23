from admin.admin import admin_site
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('frontsite.route')),
    url(r'^api/', include('api.router')),
]
