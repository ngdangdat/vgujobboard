from django.test import TestCase

from .base import *

from user.models import User, Profile

class UserTest(TestCase):
  """
  python manage.py test api.tests.UserTest --settings=core.settings.test
  """

  def test_user(self):
    credentials = {
      'email': default_email,
      'password': default_password,
      'first_name': default_first,
      'last_name': default_last,
      'profile': default_profile
    }
    data = credentials.copy()
    user_data = None

    """
    Test creating user
    """
    response = send_request('post', 'user', data=data)
    user_data = response['data']
    self.assertEqual(response['success'], True, 'Can not create user')

    user = User.objects.get(pk=user_data['id'])
    user.is_active = True
    user.save()

    """
    Test logging in user
    """ 
    response = send_request('post', 'auth', data=data)
    self.assertEqual(response['success'], True, 'Can not log in user')

    """
    Test get profile user without permission
    """
    response = send_request('get', 'user/profile')
    self.assertEqual(response['success'], False, 'Non-logged in user can get profile information')

    """
    Test get profile user with permission
    """
    response = send_request('get', 'user/profile', user=user)
    self.assertEqual(response['success'], True, 'Can not get user profile')

    """
    Test list users without permission
    """
    response = send_request('get', 'user')
    self.assertEqual(response['success'], False, 'User without permission can get user list')

    """
    Test list users without permission
    """
    response = send_request('get', 'user', user=user)
    self.assertEqual(response['success'], True, 'Logged-in user cannot get user list')
