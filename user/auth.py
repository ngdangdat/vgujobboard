from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend as BaseModelBackend

UserModel = get_user_model()

class ModelBackend(BaseModelBackend):
  """
  Custom authentication back-end allows login with email
  """
  def authenticate(self, request, email=None, password=None, **kwargs):
    if email is None:
      email = kwargs.get(UserModel.USERNAME_FIELD)
    try:
      user = UserModel._default_manager.get(email=email)
      if user.check_password(password):
        return user
    except UserModel.DoesNotExist:
      UserModel().set_password(password)