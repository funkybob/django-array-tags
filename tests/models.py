
from django.db import models

from array_tags import fields, managers


class TestModel(models.Model):
    tags = fields.TagField()
    lower_tags = fields.TagField(lower=True)

    objects = managers.TagQuerySet.as_manager()
