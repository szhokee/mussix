from rest_framework import serializers
from music.models import Music

class MusicSerializer(serializers.ModelSerializer):
    # title = serializers.CharField()

    class Meta:
        model = Music
        fields = '__all__'