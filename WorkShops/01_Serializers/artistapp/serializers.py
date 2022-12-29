from rest_framework import serializers
from .models import Artist, Album, Song, Lyric

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField() 
    album = serializers.StringRelatedField() 
    lyric = serializers.StringRelatedField()

    class Meta:
        model = Song
        # fields = "__all__"
        fields = ["name", "artist", "album", "lyric"]

class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True)
    songs = SongSerializer(many=True)

    class Meta:
        model = Album
        # fields = "__all__"
        fields = ["id", "name", "artist", "songs"]

class LyricSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lyric
        # fields = "__all__"
        fields = ["title", "content"]


