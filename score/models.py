from django.db import models
from django.contrib.auth.models import User
from solo.models import SingletonModel


class Division(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    division = models.ForeignKey(
        Division,
        verbose_name='Division'
    )

    def __str__(self):
        return self.nom


class Rencontre(models.Model):
    numero = models.IntegerField()
    date = models.DateField()
    heure = models.TimeField()

    equipeDom = models.ForeignKey(
        Equipe,
        related_name='rencontreDom',
        verbose_name='Equipe Domicile'
    )
    equipeExt = models.ForeignKey(
        Equipe,
        related_name='rencontreExt',
        verbose_name='Equipe Exterieur'
    )

    scoreDom = models.IntegerField(
        verbose_name='Score Domicile',
        null=True,
        blank=True
    )
    scoreExt = models.IntegerField(
        verbose_name='Score Exterieur',
        null=True,
        blank=True
    )

    forfaitDom = models.BooleanField(
        verbose_name='Forfait Domicile',
        default=False
    )
    forfaitExt = models.BooleanField(
        verbose_name='Forfait Exterieur',
        default=False
    )

    def __str__(self):
        return str(self.numero)


class Profil(models.Model):
    user = models.OneToOneField(User, verbose_name='Utilisateur')
    equipes = models.ManyToManyField(Equipe)

    def __str__(self):
        return self.user.username


class SiteConfiguration(SingletonModel):
    login = models.CharField(max_length=7, verbose_name='Identifiant')
    password = models.CharField(max_length=8, verbose_name='Mot de passe')
    url_ffbb = models.CharField(max_length=50, verbose_name='URL du site FFBB')

    class Meta:
        verbose_name = "Site Configuration"
