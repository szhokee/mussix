
from django.contrib import admin
from django.urls import path
from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', get_hello),
    path('musics/', get_musics),
    path('musics/<int:id>/', get_song),
    path('musics/create/', post_musics),
]
