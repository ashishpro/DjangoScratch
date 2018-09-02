from django.http import HttpResponse
from .models import Songs,Album
from .serializer import SongsSerializer,AlbumSerializer
from rest_framework import viewsets, permissions


class SongsView(viewsets.ModelViewSet):
    model = Songs
    queryset = Songs.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SongsSerializer

    def get_queryset(self):
        return self.model.objects.all()


class AlbumView(viewsets.ModelViewSet):
    model = Album
    queryset = Album.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return self.model.objects.all()
