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
        if values is None:
            return []
        values = {val.strip() for val in values}
        if self.lower:
            values = {val.lower() for val in values}
        return tuple(values)

    def contribute_to_class(self, cls, name, *args, **kwargs):
        '''
        Add a 'get_{name}_most_like' method.
        '''
        super(TagField, self).contribute_to_class(cls, name, *args, **kwargs)

        def get_most_like_by_FIELD(self, exclude_self=True, field=name):
            qset = self.__class__._default_manager.all()
            if exclude_self:
                qset = qset.exclude(pk=self.pk)
            return qset.most_like(field, getattr(self, field))

        setattr(cls, 'get_most_like_by_%s' % name, get_most_like_by_FIELD)
