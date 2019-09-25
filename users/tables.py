import django_tables2 as tables
from response.models import CareResponses


class CareTable(tables.Table):
    class Meta:
        model = CareResponses
