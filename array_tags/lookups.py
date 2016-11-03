from django.db import models


class Unnest(models.Func):
    function = 'unnest'
    arity = 1


class ArrayLength(models.Func):
    function = 'array_length'
    arity = 1
    output_field = models.IntegerField()


class Intersect(models.Func):
    template = 'array_length(ARRAY(SELECT * FROM UNNEST(%(field)s) WHERE UNNEST = ANY(%(value)s)), 1)'
    output_field = models.IntegerField()
    arity = 2

    def as_sql(self, compiler, connection, function=None, template=None):
        field_sql, field_params = compiler.compile(self.source_expressions[0])
        value_sql, value_params = compiler.compile(self.source_expressions[1])

        template = template or self.extra.get('template', self.template)
        return (
            template % {'field': field_sql, 'value': value_sql},
            field_params + value_params,
        )
