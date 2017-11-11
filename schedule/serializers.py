"""
Schedule serializer modal
"""
from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    """
    Schedule serializer
    """
    class Meta:
        model = Schedule
        fields = ['pk', 'performance', 'date_time', 'place', 'ticket']
