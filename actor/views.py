"""
Actor view modal
"""
from rest_framework import permissions, authentication, status, generics, viewsets, views
from rest_framework.response import Response

from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    """
    Actor list or create new actor
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def create(self, request, *args, **kwargs):
        """
        Create new actor
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = self.request.user
        if user.is_authenticated():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            actor = Actor.objects.create(**serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
            return Response(data=self.serializer_class(actor).data,
                            status=status.HTTP_201_CREATED, headers=headers)
        return Response(status=status.HTTP_403_FORBIDDEN)


class ActorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Update or delete information about actor
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
