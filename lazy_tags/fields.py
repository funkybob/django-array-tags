from types import MethodType

from django.contrib.postgres.fields import ArrayField
from django.db import models

from .lookups import Unnest


class TagField(ArrayField):
    def __init__(self, **kwargs):
        kwargs.setdefault('blank', True)
        super(TagField, self).__init__(models.CharField(max_length=50), **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super(TagField, self).contribute_to_class(cls, name, **kwargs)
        # - tag with counts
        # - similar items

        def all_FOO_values(cls, name=name):
            return (
                cls.objects
                .annotate(_v=Unnest(name))
                .values_list('_v', flat=True)
                .distinct()
            )
        setattr(cls, 'all_%s_values' % name, classmethod(all_FOO_values))

        def count_FOO_values(cls, name=name):
            return dict(
                cls.objects
                .annotate(_v=Unnest(name))
                .values('_v')
                .annotate(count=models.Count('*'))
                .values_list('_v', 'count')
            )
        setattr(cls, 'count_%s_values' % name, classmethod(count_FOO_values))

    def pre_save(self, model_instance, add):
        '''
        Trim whitspace and deduplicate values.
        '''
        values = super(TagField, self).pre_save(model_instance, add)
        return tuple(set(val.strip() for val in values))
