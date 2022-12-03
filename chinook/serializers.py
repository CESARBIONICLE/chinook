from rest_framework import serializers

from chinook.models import Artist, Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["name"]


class AlbumListSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(read_only=True, many=True, source="track_set")

    class Meta:
        model = Album
        fields = ["id", "title", "tracks"]


class AlbumAggregatedListSerializer(serializers.ModelSerializer):
    artist = serializers.ReadOnlyField(source="artist.name")
    total_tracks = serializers.SerializerMethodField("get_total_tracks", read_only=True)

    class Meta:
        model = Album
        fields = ["id", "title", "artist", "total_tracks"]

    def get_total_tracks(self, obj):
        return Track.objects.filter(album=obj).count()


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(read_only=True, many=True, source="track_set")

    class Meta:
        model = Album
        fields = ["title", "tracks"]


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumListSerializer(read_only=True, many=True, source="album_set")

    class Meta:
        model = Artist
        fields = ["name", "albums"]
