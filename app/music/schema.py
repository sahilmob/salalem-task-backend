import graphene
from graphene_django import DjangoObjectType

from .models import Artist, Album


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class Query(object):
    all_artists = graphene.List(ArtistType)
    artist_all_albums = graphene.List(AlbumType, artist=graphene.Int())

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_artist_all_albums(self, info, **kwargs):
        artist = kwargs.get('artist')
        return Album.objects.filter(artist__exact=artist)
