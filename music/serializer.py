from rest_framework import serializers
from .models import Songs,Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['album_title', 'year', 'genre', 'artist', 'album_logo']


class SongsSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = Songs
        fields = ['album', 'title']
