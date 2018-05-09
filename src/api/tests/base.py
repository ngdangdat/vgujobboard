import json
import string
from urllib.parse import urlencode

from rest_framework.test import APIClient

default_email = 'email@yopmail.com'
default_password = 'Admin@!@#'
default_first = 'Dat'
default_last = 'Nguyen'
default_profile = {
  'gender': 5,
  'major_intake': 'Test',
  'state': 'Ahihi',
  'country': 'VN',
  'office': 'Test',
  'job_title': 'Test',
  'message': 'Ahihi',
}

def to_json(content):
  chars = content.decode('utf-8')
  return json.loads(chars)

def send_request(method='get', path='', data={}, format='json', client=None, user=None, params={}, *args, **kwargs):
  if client is None:
    client = APIClient()
  if user is not None:
    client.credentials(HTTP_AUTHORIZATION='Token ' + user.token.key)
  fn = getattr(client, method)
  endpoint = '/api'
  if path.startswith('/'):
    endpoint += path
  else:
    endpoint += '/' + path
  if params:
    endpoint += '?%s' % urlencode(params)
  if 'content_type' in kwargs:
    format = None
  response = fn(endpoint, data, format, **kwargs)
  return to_json(response.content)
