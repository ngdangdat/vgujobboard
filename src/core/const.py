
class Const(object):
  choices = []

  def __setattr__(self, *_):
    raise Exception('Cannot set value for constant')

  @classmethod
  def get_value(self, name):
    name = name.lower()
    for item in self.choices:
      if item[1].lower() == name:
        return item[0]

  @classmethod
  def get_name(self, value):
    if not isinstance(value, int):
      value = int(value)
    for item in self.choices:
      if item[0] == value:
        return item[1]
