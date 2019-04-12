import graphene
from graphene_django import DjangoObjectType

from .models import Artist, Album, Song


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class SongType(DjangoObjectType):
    class Meta:
        model = Song


class Query(object):
    all_artists = graphene.List(ArtistType)
    artist_all_albums = graphene.List(AlbumType, artist=graphene.Int())
    album_all_songs = graphene.List(SongType, album=graphene.Int())

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_artist_all_albums(self, info, **kwargs):
        artist = kwargs.get('artist')
        return Album.objects.filter(artist__exact=artist)

    def resolve_album_all_songs(self, info, **kwargs):
        album = kwargs.get('album')
        print(album)
        return Song.objects.filter(album__exact=album)
