"""
News view modal
"""
from rest_framework import generics

from .models import News
from .serializers import NewsSerializer


class NewsListCreateView(generics.ListCreateAPIView):
    """
    News list or create new news
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete news
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
