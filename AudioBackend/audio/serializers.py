from rest_framework.serializers import ModelSerializer
from .models import songs
import mutagen   # importing mutagen to get the size of a audio file
from rest_framework import serializers

class SongSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['audio']=self.context['request'].FILES['audio']  # saving audio in audio field of dictionary
        validated_data['name']=self.context['request'].FILES['audio'].name   # getting name by name attribute and saving in name variable in dictionary
        validated_data['size']=round(self.context['request'].FILES['audio'].size/1048576,2) # getting and saving size in size field in dictionary
        validated_data['extension']=self.context['request'].FILES['audio'].name.split('.')[-1] # saving extension in dictionary
        validated_data['duration']=round(mutagen.File(self.context['request'].FILES['audio']).info.length/60,2) # getting duration with then help of mutagen library
        return songs.objects.create(**validated_data)
    class Meta:
        model=songs
        fields='__all__'

    def validate_audio(self,value):      # validating if the file is not audio type then raise error
        if value.content_type!="audio/mpeg":
            raise serializers.ValidationError("file type not audio")
        return value