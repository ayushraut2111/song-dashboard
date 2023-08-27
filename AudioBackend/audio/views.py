from rest_framework.viewsets import ModelViewSet
from .models import songs
from .serializers import SongSerializer
from rest_framework.response import Response
from django.db.models import Sum



class song_api(ModelViewSet):
    
    queryset = songs.objects.all()
    serializer_class = SongSerializer

    def create(self, request, *args, **kwargs):
        ser = SongSerializer(data=request.data, context={'request': request})    # in serializer sending request with the help of context
        if ser.is_valid():
            ser.save()
        if request.FILES['audio'].content_type!="audio/mpeg":   # checking if it is not a audio type then return a warning   
            return Response({"msg":"file is not audio type"})
        countdur=songs.objects.aggregate(Sum('duration')) # get total duration by aggregate propery
        if countdur['duration__sum'] > 10:    # checking if the length of audio file is greater than 10 minutes or not the return a warning
            return Response({"msg": "Song Uploaded,Total duration of all the songs exceeds 10 minutes"})
        else:
            return Response({"msg": "Song uploaded"})
