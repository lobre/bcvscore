from django.shortcuts import render
from score.models import Rencontre


def home(request):
    rencontres = Rencontre.objects.all().order_by('-date')
    return render(
        request,
        'score/home.html',
        locals()
    )

