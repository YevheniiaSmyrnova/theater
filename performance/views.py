"""
Performance view modal
"""
from rest_framework import generics

from .models import Performance
from .serializers import PerformanceSerializer


class PerformanceListCreateView(generics.ListCreateAPIView):
    """
    Performance list or create new performance
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class PerformanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete information about performance
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
