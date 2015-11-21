django-array-tags
=================

A simple Tag solution for Django using `django.contrib.postgres.fields.ArrayField`.

Usage
-----

Add the ArrayField to your model:

    from array_tags.fields import TagField

    class MyModel(models.Model):
        tagss = TagField()


Now you have tags!  Values will be stripped and de-duplicated on save.


For convenience, there is also a `TagQuerySet` which adds two methods:

`all_tag_values(name)`

Returns all tuple the tags in objects in the current queryset from the TagField called `name`.

`count_tag_values(name)`

Returns a dict of tags and how many objects have each tag in the queryset.
