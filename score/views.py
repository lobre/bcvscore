from django.shortcuts import render
from score.models import Rencontre, Division, Equipe, Profil
from django.contrib.auth.models import User
from django.db.models import Q
import datetime

from rest_framework import viewsets
from score.permissions import CoachATeam
from score.serializers import DivisionSerializer, EquipeSerializer, RencontreSerializer, UserSerializer, ProfilSerializer


def home(request):
    home = True
    title = "Résultats"

    rencontres = Rencontre.objects.filter(
        date__lte=datetime.date.today()
    ).order_by(
        '-date',
        '-heure'
    )

    if 'q' in request.GET:
        q = request.GET['q']
        query = Q(equipeDom__nom__icontains=q) | Q(equipeExt__nom__icontains=q) | Q(equipeDom__division__nom__icontains=q)
        rencontres = rencontres.filter(query)

    return render(
        request,
        'score/results.html',
        locals()
    )


def upcoming(request):
    home = False
    title = "Matchs à venir"

    rencontres = Rencontre.objects.filter(
        date__gt=datetime.date.today()
    ).order_by(
        'date',
        'heure'
    )

    print(rencontres)

    if 'q' in request.GET:
        q = request.GET['q']
        query = Q(equipeDom__nom__icontains=q) | Q(equipeExt__nom__icontains=q) | Q(equipeDom__division__nom__icontains=q)
        rencontres = rencontres.filter(query)

    return render(
        request,
        'score/results.html',
        locals()
    )


class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class RencontreViewSet(viewsets.ModelViewSet):
    queryset = Rencontre.objects.all()
    serializer_class = RencontreSerializer
    permission_classes = (CoachATeam,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfilViewSet(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
