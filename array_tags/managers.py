from django.db.models import Count, QuerySet, F

from .lookups import Unnest, Intersect


class TagQuerySet(QuerySet):
    '''
    Mix into your tagged model to provide extra helpers
    '''
    def all_tag_values(self, name):
        return tuple(
            self.order_by()
            .annotate(_v=Unnest(name))
            .values_list('_v', flat=True)
            .distinct()
        )

    def count_tag_values(self, name):
        return dict(
            self.order_by()
            .annotate(_v=Unnest(name))
            .values('_v')
            .annotate(count=Count('*'))
            .values_list('_v', 'count')
        )

    def most_like(self, field, tags):
        '''
        '''
        return (
            self.order_by()
            .annotate(
                similarity=Intersect(F(field), tags)
            )
            .order_by('-similarity')
        )
