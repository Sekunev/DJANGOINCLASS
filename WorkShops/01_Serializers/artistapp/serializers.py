from rest_framework import serializers
from .models import Artist, Album, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True) 
    
    class Meta:
        model = Album
        # fields = "__all__"
        fields = ["id", "name", "artist" ]

class SongSerializer(serializers.ModelSerializer):
    # artist = serializers.StringRelatedField(many=True) 
    # album = serializers.StringRelatedField(many=True) 

    class Meta:
        model = Song
        # fields = "__all__"
        fields = ["id", "name", "artist", "album"]