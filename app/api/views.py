from rest_framework.viewsets import ModelViewSet
from api.serializers import ArtistSerializer
from api.models import Artist


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
