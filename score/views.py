from django.shortcuts import render
from score.models import Rencontre
from django.db.models import Q
import datetime


def home(request):
    home = True
    title = "Résultats"

    today = datetime.date.today()
    next_sunday = today + datetime.timedelta(6-today.weekday())

    rencontres = Rencontre.objects.filter(
        date__lte=next_sunday
    ).order_by(
        '-date',
        '-heure'
    )

    if 'q' in request.GET:
        q = request.GET['q']
        query = Q(equipeDom__nom__icontains=q) | Q(equipeExt__nom__icontains=q)
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
        date__gte=datetime.date.today()
    ).order_by(
        'date',
        'heure'
    )

    if 'q' in request.GET:
        q = request.GET['q']
        query = Q(equipeDom__nom__icontains=q) | Q(equipeExt__nom__icontains=q)
        rencontres = rencontres.filter(query)

    return render(
        request,
        'score/results.html',
        locals()
    )

