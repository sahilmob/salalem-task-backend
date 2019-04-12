import graphene
from graphene_django import DjangoObjectType

from .models import Artist


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
