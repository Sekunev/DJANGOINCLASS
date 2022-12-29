from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, LyricSerializer

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import mixins, GenericAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
def home(request):
    return HttpResponse('This is my Page..')

#***! artist_api  ['GET', 'POST'] ***/
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

#***! album_api  ['GET', 'POST'] ***/
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

#***! song_api  ['GET', 'POST'] ***/
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

#! /*** DETAİL TEK OBJEYE YAPILAN İŞLEMLER  BİRLEŞTİRİLMİŞ***/

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

# * ================================
# todo      CLASS BASED VIEWS
# * ================================

class ArtistListCreate(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Album {serializer.validated_data.get('name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#! /*** DETAİL TEK OBJEYE YAPILAN İŞLEMLER  ***/

class ArtistDetail(APIView):
    def get_obj(self, pk):
        return get_object_or_404(Artist, id=pk)
    def get(self, request, pk):
        artist = self.get_obj(pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    def put(self, request, pk):
        artist = self.get_obj(pk)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {
                "message" : "update Artist"
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        artist = self.get_obj(pk)
        artist.delete()
        message = {
            "message": 'Artist deleted succesfully....'
        }
        return Response(message)

# * ================================
# todo      GENERIC API VIEWS and Mixins
# * ================================

class ArtistGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)
    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *arg, **kwargs):
        return self.retrieve(request, *arg, **kwargs)

    def put(self, request, *arg, **kwargs):
        return self.update(request, *arg, **kwargs)

    def delete(self, request, *arg, **kwargs):
        return self.destroy(request, *arg, **kwargs)

#* #################### 
#! 4- CONCRETE VIEWS  
#* ####################

class ArtistCV(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

#* #################### 
#! 5- VIEWSET  (@action)  
#* ####################

# artist sayısı
class ArtistMVS(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=False, methods=["GET"])
    def artist_count(self, request):
        count = {
            "Artist-count" : self.queryset.count()
        }
        return Response(count)


#! Albumlerdeki şarkılar.
class AlbumMVS(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    print(queryset)

    @action(detail=True)
    def song_names(self, request, pk=id):
        album = self.get_object()
        songss = album.songs.all()
        print(songss)
        return Response([i.name for i in songss])
