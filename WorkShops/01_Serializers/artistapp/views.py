from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, LyricSerializer, SongLyricSerializer

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
        print(serializer.data)
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

#! /*** DETAİL TEK OBJEYE YAPILAN İŞLEMLER  ***/

@api_view(['GET'])
def artist_detail(request, pk):
    # pk : Çağırılan objenin id'si. Primary key.
    # student = Student.objects.get(id=pk)
    # Student tablosundaki id'si pk'ya eşit olan
    # Yukarıdaki yöntemi uyguladığımızda id'si olmayan bir sorgu yapıldığında hata alırız. Bunu önlemek için 2 yöntem var.
    # 1.si try except
    #! 2. get_object_or_404 yöntemi. Bu yöntem id'si x olanı çek yoksa 404 not found hatası ver demek oluyor.
    artist = get_object_or_404(Artist, id=pk)
    serializer = ArtistSerializer(artist)
    # tek eleman olduğu için many=True yazmadık.
    return Response(serializer.data)

#! /*** PUT  ***/
@api_view(['PUT'])
def artist_update(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    serializer = ArtistSerializer(instance=artist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {
            "message" : "update Artist"
        }
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! /*** DELETE  ***/
@api_view(['DELETE'])
def artist_delete(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    artist.delete()
    message = {
        "message": 'Artist deleted succesfully....'
    }
    return Response(message)

@api_view(['GET', 'DELETE', 'PUT'])
def artist_get_put_delete(request, pk):
    artist = get_object_or_404(Artist, id=pk)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        artist.delete()
        message = {
            "message": 'Artist deleted succesfully....'
            }
        return Response(message)
    elif request.method == 'PUT':
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message" : "update Artist"
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def SongLyric(request):
        songs = Song.objects.all()
        serializer = SongLyricSerializer(songs, many=True)
        print(serializer.data)
        return Response(serializer.data)
