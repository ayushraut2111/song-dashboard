from rest_framework.viewsets import ModelViewSet
from .models import songs
from .serializers import SongSerializer
from rest_framework.response import Response
from mutagen.wave import WAVE

class song_api(ModelViewSet):
    queryset=songs.objects.all()
    serializer_class=SongSerializer

    def create(self, request, *args, **kwargs):
        print(request.FILES['audio'].content_type)
        ser=SongSerializer(data=request.data,context={'request':request})
        if ser.is_valid():
            ser.save()
        return Response({"msg":"created"})