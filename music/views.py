from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.models import Music
from music.serializers import MusicSerializer
# Create your views here.


@api_view(['GET'])
def get_hello(request):
    # print(dir(request))
    # print(request.user)
    return Response('Hello World')


@api_view(['GET'])
def get_musics(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    # print(musics)
    return Response(serializer.data)


@api_view(['GET'])
def get_song(request, id):
    try:
        song = Music.objects.get(id=id)

    except Music.DoesNotExist:
        return Response('Нет такой песни дорогой')

    serializer = MusicSerializer(song, many=False)
    # print(musics)
    return Response(serializer.data)


@api_view(['POST'])
def post_musics(request):
    print(request.data)
    # musics = Music.objects.all()
    serializer = MusicSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    # print(musics)
    return Response(serializer.data)




# DELETE, PUT(обновляет), PATCH (частично)
# api_view(['PUT', 'PATH'])