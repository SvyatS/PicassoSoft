from django_filters import rest_framework as filters

from .models import Policeorders


class PoliceOrdersFilter(filters.FilterSet):
    date_from = filters.IsoDateTimeFilter(field_name='reportdate', lookup_expr='gte')
    date_to = filters.IsoDateTimeFilter(field_name='reportdate', lookup_expr='lte')

    class Meta:
        model = Policeorders
        fields = ('date_from', 'date_to')