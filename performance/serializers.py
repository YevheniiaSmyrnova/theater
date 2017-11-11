"""
Performance serializer modal
"""
from rest_framework import serializers
from .models import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    """
    Performance serializer
    """
    class Meta:
        model = Performance
        fields = ['pk', 'name', 'photo', 'actors', 'producer', 'duration',
                  'sort_description', 'description']
