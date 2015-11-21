from django.db import models
from django.db.models.lookups import Transform
from django.utils.functional import cached_property


class Unnest(models.Func):
    function = 'unnest'
