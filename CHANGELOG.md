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
