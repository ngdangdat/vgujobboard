from django.urls import path, include
from . import views

app_name = 'frontsite'

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login', views.user_login, name='user_login'),
]
