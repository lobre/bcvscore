from django.db import models

class Division(models.Model):
    nom = models.CharField(max_length=10)

    def __str__(self):
        return self.nom


class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    division = models.ForeignKey(Division)

    def __str__(self):
        return self.nom

class Rencontre(models.Model):
    numero = models.IntegerField()
    date = models.DateField()
    heure = models.TimeField()

    equipeDom = models.ForeignKey(Equipe, related_name='equipeDom')
    equipeExt = models.ForeignKey(Equipe, related_name='equipeExt')

    scoreDom = models.IntegerField()
    scoreExt = models.IntegerField()

    forfaitDom = models.BooleanField()
    forfaitExt = models.BooleanField()
