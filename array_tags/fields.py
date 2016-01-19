from django.contrib.postgres.fields import ArrayField
from django.db import models


class TagField(ArrayField):
    def __init__(self, **kwargs):
        self.lower = kwargs.pop('lower', False)
        kwargs.setdefault('blank', True)
        kwargs.setdefault('base_field', models.CharField(max_length=50))
        super(TagField, self).__init__(**kwargs)

    def pre_save(self, model_instance, add):
        '''
        Trim whitspace and deduplicate values.
        '''
        values = super(TagField, self).pre_save(model_instance, add)
        values = {val.strip() for val in values}
        if self.lower:
            values = {val.lower() for val in values}
        return tuple(values)
