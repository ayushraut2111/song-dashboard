from rest_framework.viewsets import ModelViewSet
from .models import songs
from .serializers import SongSerializer
from rest_framework.response import Response
import mutagen  # using mutagen to get the size of a audio file


class song_api(ModelViewSet):
    queryset = songs.objects.all()
    serializer_class = SongSerializer

    def create(self, request, *args, **kwargs):
        # in serializer sending request with the help of context
        ser = SongSerializer(data=request.data, context={'request': request})
        print(request.FILES)
        if ser.is_valid():
            ser.save()
        # checking if the length of audio file is greater than 10 minutes or not
        if round(mutagen.File(request.FILES['audio']).info.length/60, 2) > 10:
            return Response({"msg": "Duration Exceeds"})
        else:
            return Response({"msg": ""})
