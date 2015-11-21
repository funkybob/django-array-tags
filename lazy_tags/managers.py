from django.db.models import Count, QuerySet

from .lookups import Unnest


class TagQuerySet(QuerySet):
    '''
    Mix into your tagged model to provide extra helpers
    '''
    def all_tag_values(self, name):
        return tuple(
            self
            .annotate(_v=Unnest(name))
            .values_list('_v', flat=True)
            .distinct()
        )

    def count_tag_values(self, name):
        return dict(
            self
            .annotate(_v=Unnest(name))
            .values('_v')
            .annotate(count=Count('*'))
            .values_list('_v', 'count')
        )
