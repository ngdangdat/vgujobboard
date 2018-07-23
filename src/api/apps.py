from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        self.patch_rest_framework()

    def patch_rest_framework(self):
        from rest_framework import response, exceptions, serializers, validators

        from api.http import Response
        from api.exceptions import __api_exc_init__, __validator_exc_ini__

        # Override response format
        response.Response = Response

        # Patch for rest_framework
        exceptions.APIException.__init__ = __api_exc_init__
        exceptions.ValidationError.__init__ = __validator_exc_ini__
