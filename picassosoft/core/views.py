from rest_framework import generics
from django_filters import rest_framework as filters

from .models import Policeorders
from .serializers import PoliceOrdersSerializer
from .filters import PoliceOrdersFilter


class PoliceOrdersListView(generics.ListAPIView):
    queryset = Policeorders.objects.all()
    serializer_class = PoliceOrdersSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = PoliceOrdersFilter
