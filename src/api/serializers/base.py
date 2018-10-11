from collections import Mapping, OrderedDict

from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework import serializers
from rest_framework.serializers import ValidationError, empty
from rest_framework import fields as rest_fields
from rest_framework.settings import api_settings


def get_code_from_exc(exc):
  """
  Patch inject error code
  """
  assert isinstance(exc, (ValidationError, DjangoValidationError))
  code = getattr(exc, 'code', api_settings.NON_FIELD_ERRORS_KEY)
  if isinstance(exc, DjangoValidationError):
    return { code: ' '.join(list(exc.messages)) }
  elif isinstance(exc.detail, dict):
    return {
      key: value if isinstance(value, (list, dict)) else [value]
      for key, value in exc.detail
    }
  elif isinstance(exc.detail, list):
    return { code: ' '.join(exc.detail) }
  return { code: exc.detail }

class Serializer(serializers.Serializer):
  """
  Overwrite to inject error code
  """
  def to_internal_value(self, data):
    if not isinstance(data, dict):
      message = self.error_messages['invalid'].format(
          datatype=type(data).__name__
      )
      raise ValidationError({
          api_settings.NON_FIELD_ERRORS_KEY: [message]
      })

    def append_error(field, key, error):
      if errors.get(field, None) is None:
        errors[field] = dict()
      errors[field][key] = error

    ret = OrderedDict()
    errors = OrderedDict()
    fields = self._writable_fields

    for field in fields:
      validate_method = getattr(self, 'validate_' + field.field_name, None)
      primitive_value = field.get_value(data)

      try:
        validated_value = field.run_validation(primitive_value)
        if validate_method is not None:
          validated_value = validate_method(validated_value)
      except ValidationError as exc:
        code = getattr(exc, 'code', None)
        if code is not None:
          append_error(field.field_name, code, ' '.join(exc.detail))
        else:
          errors[field.field_name] = ' '.join(exc.detail)
      except DjangoValidationError as exc:
        errors[field.field_name] = ' '.join(exc.messages)
      except serializers.SkipField:
        pass
      else:
        rest_fields.set_value(ret, field.source_attrs, validated_value)

      if errors:
        raise ValidationError(errors)

    return ret


  def run_validation(self, data=empty):
    (is_empty_value, data) = self.validate_empty_values(data)
    if is_empty_value:
      return data

    value = self.to_internal_value(data)
    try:
      self.run_validators(value)
      value = self.validate(value)
      assert value is not None, '.validate() should return the validated data'
    except (ValidationError, DjangoValidationError) as exc:
      code = getattr(exc, 'code', None)
      raise ValidationError(detail=get_code_from_exc(exc), code=code)

    return value


class ModelSerializer(Serializer, serializers.ModelSerializer):
  pass
