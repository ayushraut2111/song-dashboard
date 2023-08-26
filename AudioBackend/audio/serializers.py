from rest_framework.serializers import ModelSerializer
from .models import songs

class SongSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['audio']=self.context['request'].FILES['audio']
        # validated_data['name']=self.context['request'].FILES['audio'].name
        return songs.objects.create(**validated_data)
    class Meta:
        model=songs
        fields='__all__'