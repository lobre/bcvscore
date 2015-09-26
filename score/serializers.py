from score.models import Division, Equipe, Rencontre, Profil
from django.contrib.auth.models import User
from rest_framework import serializers


class DivisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Division
        fields = ('id', 'nom')


class EquipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipe
        fields = ('id', 'nom', 'division')


class RencontreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rencontre
        fields = (
            'id',
            'numero',
            'date',
            'heure',
            'equipeDom',
            'equipeExt',
            'scoreDom',
            'scoreExt',
            'forfaitDom',
            'forfaitExt'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class ProfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profil
        fields = ('id', 'user', 'equipes')
