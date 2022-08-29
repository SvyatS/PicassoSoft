from rest_framework import serializers

from .models import Policeorders


class PoliceOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Policeorders
        fields = '__all__'
