from django.urls import path, include
from . import views

app_name = 'frontsite'

urlpatterns = [
    path('', views.index, name='index'),
]
