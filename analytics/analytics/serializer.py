from rest_framework import serializers
from analytics.models import PollutionData

class PollutionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollutionData
        fields = '__all__'