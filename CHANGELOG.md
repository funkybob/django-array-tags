# 0.2.0

Make compatible with Django 1.10
Set output_field on ArrayLength db func

# 0.1.7

Change manager methods to return querysets.

# 0.1.6

Added `get_most_like_by_FIELD` helper method.
Safely replace None with []

# 0.1.5

Added `lower` option to `TagField`

# 0.1.4

Added `TagQuerySet.most_like` method.

# 0.1.3

Remove debug kruft from fixing previous bug.

# 0.1.2

Ensure we remove ordering from querysets we're going to count to avoid extra
fields in the group by ruining the count.

# 0.1.1

Fixed setting base_field so it didn't break Migrations
Removed contribute_to_class

# 0.1

Initial release
