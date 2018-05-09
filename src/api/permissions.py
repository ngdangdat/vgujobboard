from rest_framework import permissions
from rest_framework.utils import formatting

def get_view_name(view_cls, suffix=None):
    """
    Given a view class, return a textual name to represent the view.
    This name is used in the browsable API, and in OPTIONS responses.

    This function is the default for the `VIEW_NAME_FUNCTION` setting.
    """
    name = view_cls.__name__
    name = formatting.remove_trailing_string(name, 'View')
    name = formatting.remove_trailing_string(name, 'ViewSet')
    name = formatting.camelcase_to_spaces(name)
    if suffix:
        name += ' ' + suffix

    return name

def get_action(request, view):
  method = request.method.lower()
  view_action = getattr(view, 'view_action', '')
  method = method + '_' + get_view_name(view.__class__)
  if view_action != '':
    method += '_' + view_action
  return method.lower()

class IsAuthenticated(permissions.IsAuthenticated):
  """
  Permission check for API access
  """
  exceptions = [
    'post_user',
  ]

  def has_permission(self, request, view):
    if get_action(request, view) in self.exceptions:
      return True
    return request.user and request.user.is_authenticated
