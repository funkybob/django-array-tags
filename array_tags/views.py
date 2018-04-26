from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.views.generic import View


class AutoSuggestView(View):
    def get(self, request, label):
        try:
            model_name, field_name = getattr(settings, 'ARRAYTAG_AUTOCOMPLETE_MODELS', {})[label]
        except KeyError:
            raise Http404
        except (TypeError, ValueError):
            raise ImproperlyConfigured('ARRAYTAG_AUTOCOMPLETE_MODELS must be a dict of 2-tuples of (model-name, field-name)')

        model = apps.get_model(model_name)

        qset = model.default_manager.all_tag_values(field_name)

        q = request.GET.get('q', None)
        if q:
            qset = qset.filter(_v__ilike=q)

        limit = getattr(settings, 'ARRAYTAG_AUTOCOMPLETE_LIMIT', 10)

        return JsonResponse({'data': list(qset[:limit])})