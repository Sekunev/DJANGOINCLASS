from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def home(request):
    return HttpResponse('This is my Page..')

@api_view(['GET', 'POST'])
def artist_api(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Artist {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def album_api(request):
    if request.method == 'GET':
        artists = Album.objects.all()
        serializer = AlbumSerializer(artists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Album {serializer.validated_data.get('name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def song_api(request):
    if request.method == 'GET':
        artists = Song.objects.all()
        serializer = SongSerializer(artists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Album {serializer.validated_data.get('name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)