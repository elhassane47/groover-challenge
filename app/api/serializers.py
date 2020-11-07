from rest_framework import serializers
from api.models import Artist


class ArtistSerializer(serializers.ModelSerializer):

    #the id field in spotify api is stored as spotify_id in our model

    id = serializers.CharField(source='spotify_id')

    class Meta:
        model = Artist
        fields = ('pk', 'name', 'href', 'id', 'type', 'uri', 'external_urls',)


