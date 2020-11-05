from django.urls import path, include
from api.views import ArtistViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('artists', ArtistViewSet, basename='artists')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]