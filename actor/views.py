"""
Actor view modal
"""
from rest_framework import generics

from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    """
    Actor list or create new actor
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete information about actor
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
