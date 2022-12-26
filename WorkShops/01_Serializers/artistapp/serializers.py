from rest_framework import serializers
from .models import Artist, Album, Song, Lyric

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(many=True) 

    
    class Meta:
        model = Album
        # fields = "__all__"
        fields = ["id", "name", "artist"]

class LyricSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lyric
        # fields = "__all__"
        fields = ["title", "content"]

class SongSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField() 
    album = serializers.StringRelatedField() 
    lyric = serializers.StringRelatedField()

    class Meta:
        model = Song
        # fields = "__all__"
        fields = ["id", "name", "artist", "album", "lyric"]

class SongLyricSerializer(serializers.ModelSerializer):
    items = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Lyric
        fields = ['title', 'content']

"""
class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['text', 'is_completed']

class ToDoListSerializer(serializers.ModelSerializer):
    items = ToDoItemSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ['title', 'items']
"""