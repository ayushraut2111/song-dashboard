from rest_framework.serializers import ModelSerializer
from .models import songs

class SongSerializer(ModelSerializer):
    class Meta:
        model=songs
        fields='__all__'