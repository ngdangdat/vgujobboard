from django.db import models
from django.forms.models import model_to_dict

class ModelDiffMixin(models.Model):
    """
    A model mixin that tracks model fields values and provide some useful api
    to know what fields have been changed.
    """

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
    """
    Get changed fields
    :return: list
    """
        return [k for k in self.diff.keys()]

    def get_field_diff(self, field):
    """
    Return diff for a field if it's changed. Otherwise, None is returned.
    :param field: str
    """
        return self.diff.get(field, None)

    def save(self, *args, **kwargs):
        """
        Save model
        :param kwargs: update_dict set initial state
        """
        super(ModelDiffMixin, self).save(*args, **kwargs)
        if 'update_dict' in kwargs and kwargs['update_dict']:
            self.__initial = self._dict
    
    @property
    def _dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])


    class Meta:
        abstract = True
