from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.urls import reverse
from requests.exceptions import HTTPError

from api.serializers import ArtistSerializer
from api.models import Artist
from api.spotify_api import SpotifyApi
from api.spotify_auth import SpotifyAuth
from django.http.response import HttpResponseRedirect
import pdb


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    auth_api = SpotifyAuth()

    @action(detail=False, methods=['GET'])
    def new_releases(self, request):

        tokens = request.session.get('tokens')
        # if the token expired in session =>redirect to login
        if not tokens:
            return HttpResponseRedirect(redirect_to=reverse('api:spotify-login'))

        sp = SpotifyApi(token=tokens.get('access_token'))

        try:
            data = sp.artists_new_relases()

        except HTTPError:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={"message": "invalid spotify token"})

            # refresh_token = tokens.get('refresh_token')
            # token = self.auth_api.refreshAuth(refresh_token)
            # sp.set_token(token)
            # data = sp.artists_new_relases()
            # HttpResponseRedirect(redirect_to=reverse('api:spotify-login'))
        else:
            serializer = ArtistSerializer(data=data, many=True)
            if serializer.is_valid():
                try:
                    serializer.save()
                #     already existed artists with this spotify_id
                except IntegrityError as e:
                    pass
                finally:
                    return Response(status=status.HTTP_201_CREATED, data={"new release": serializer.data})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def callback(request):

    code = request.GET.get('code')
    error = request.GET.get('error')
    auth_api = SpotifyAuth()

    if error:
        payload = {
            'grant_type': 'authorization_code',
            'error': error,

        }
        return JsonResponse(status=status.HTTP_401_UNAUTHORIZED, data=payload)
    else:

        resp = auth_api.getUserToken(code)
        request.session['tokens'] = resp

        return JsonResponse(
            status=status.HTTP_200_OK,
            data={'message': "you are successfully logged in Spotify api",
                  'tokens': resp,
                  "new releases endpoint": reverse(('api:artists-new-releases'))})


def login_spotify(request):

    auth_api = SpotifyAuth()
    code_url = auth_api.getUser()

    return HttpResponseRedirect(redirect_to=code_url)