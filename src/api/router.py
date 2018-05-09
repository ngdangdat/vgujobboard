from django.conf.urls import url, include
from rest_framework import routers
from api.views import AuthViewSet, UserViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'auth', AuthViewSet, base_name='Auth')
router.register(r'user', UserViewSet, base_name='User')

urlpatterns = [
  url(r'^', include(router.urls)),
]
