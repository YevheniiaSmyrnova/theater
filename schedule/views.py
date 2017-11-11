"""
Schedule view modal
"""
from rest_framework import generics

from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleListCreateView(generics.ListCreateAPIView):
    """
    Schedule list or create new record
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete information in schedule
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
