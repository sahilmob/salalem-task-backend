import graphene
from graphene_django import DjangoObjectType

from .models import Artist


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class Query(object):
    all_artists = graphene.List(ArtistType)

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()
