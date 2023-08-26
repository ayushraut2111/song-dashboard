from rest_framework.serializers import ModelSerializer
from .models import songs
import mutagen   # importing mutagen to get the size of a audio file

class SongSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['audio']=self.context['request'].FILES['audio']
        validated_data['name']=self.context['request'].FILES['audio'].name
        validated_data['size']=round(self.context['request'].FILES['audio'].size/1048576,2)
        validated_data['extension']=self.context['request'].FILES['audio'].name.split('.')[-1]
        validated_data['duration']=round(mutagen.File(self.context['request'].FILES['audio']).info.length/60,2)
        return songs.objects.create(**validated_data)
    class Meta:
        model=songs
        fields='__all__'