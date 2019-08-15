from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import SongSerializer
from .models import Songs

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
        