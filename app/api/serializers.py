from rest_framework import serializers
from api.models import Artist


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('pk', 'name', 'href', 'spotify_id', 'type', 'uri', 'external_urls',)


