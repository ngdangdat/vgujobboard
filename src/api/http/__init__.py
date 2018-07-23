from django.http.response import JsonResponse

class Response(JsonResponse):
  def __init__(self, data={}, errors=[], status=200, success=True, headers={}, **kwargs):
    if status > 309:
      success = False
    data = dict(
      data=data,
      errors=errors,
      status=status,
      success=success,
    )
    super(Response, self).__init__(data, status=status, **kwargs)
    if headers:
      for key, value in headers.items():
        self[key] = value
