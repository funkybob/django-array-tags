
from django.db import models

from lazy_tags import fields


class TestModel(models.Model):
    tags = fields.TagField()
