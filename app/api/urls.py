from django.urls import path, include
from api.views import ArtistViewSet, callback, login_spotify
from rest_framework import routers

router = routers.DefaultRouter()

router.register('artists', ArtistViewSet, basename='artists')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('auth/callback', callback,name='spotify-callback'),
    path('login_spotify', login_spotify, name='spotify-login')
]