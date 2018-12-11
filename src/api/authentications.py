from rest_framework import authentication

from api.models import Token

class TokenAuthentication(authentication.TokenAuthentication):
  """
  Custom Token authentication
  """
  model = Token

  def authenticate_credentials(self, key):
    model = self.get_model()
    try:
      token = model.objects.get(key=key)
    except model.DoesNotExist:
      return None
    if not token.user.is_active:
      return None
    return (token.user, token)

class SessionAuthentication(authentication.SessionAuthentication):
  """
  Custom Session Authentication
  """
  pass
  # def enforce_csrf(self, request):
  #   return
