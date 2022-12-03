from rest_framework import viewsets, permissions

from chinook.models import Artist, Album
from chinook.serializers import (
    ArtistListSerializer,
    ArtistSerializer,
    AlbumSerializer,
    AlbumListSerializer,
    AlbumAggregatedListSerializer,
)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by("name")
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return ArtistListSerializer
        return super().get_serializer_class()


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by("title")
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            if self.request.GET.get("aggregated", None):
                return AlbumAggregatedListSerializer
            return AlbumListSerializer
        return super().get_serializer_class()
