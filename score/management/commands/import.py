from django.core.management.base import BaseCommand
from django.conf import settings
from score.models import Division, Equipe, Rencontre
import csv
import datetime


class Command(BaseCommand):
    help = 'Commande pour importer les données'

    def handle(self, *args, **options):
        self._downloadDataFile()
        self._importInDjango()

    def _importInDjango(self):
        """ Import data to django from csv """

        with open(settings.DATA_PATH, 'r', encoding='latin-1') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for raw in reader:

                # Créer ou mettre à jour la division
                division, created = Division.objects.get_or_create(
                    nom=raw['Division']
                )
                if created:
                    self.stdout.write(
                        'Divion {} ajoutée'.format(division.nom)
                    )

                # Créer ou mettre à jour les équipes
                equipeDom, created = Equipe.objects.get_or_create(
                    nom=raw['Equipe 1'],
                    defaults={
                        'division': division
                    }
                )
                if created:
                    self.stdout.write(
                        'Equipe {} ajoutée'.format(equipeDom.nom)
                    )

                equipeExt, created = Equipe.objects.get_or_create(
                    nom=raw['Equipe 2'],
                    defaults={
                        'division': division
                    }
                )
                if created:
                    self.stdout.write(
                        'Equipe {} ajoutée'.format(equipeExt.nom)
                    )

                # Créer ou mettre à jour la rencontre
                scoreDom = 0 if raw['Score 1'] == '' else int(raw['Score 1'])
                scoreExt = 0 if raw['Score 2'] == '' else int(raw['Score 2'])
                forfaitDom = True if raw['Forfait 1'] == 'true' else False
                forfaitExt = True if raw['Forfait 2'] == 'true' else False
                date = datetime.datetime.strptime(raw['Date de rencontre'], '%d/%m/%Y')
                heure = datetime.datetime.strptime(raw['Heure'], '%H:%M')
                rencontre, created = Rencontre.objects.get_or_create(
                    numero=int(raw['N° de match']),
                    date=date,
                    heure=heure,
                    equipeDom=equipeDom,
                    equipeExt=equipeExt,
                    defaults={
                        'scoreDom': scoreDom,
                        'scoreExt': scoreExt,
                        'forfaitDom': forfaitDom,
                        'forfaitExt': forfaitExt,
                    }
                )
                if created:
                    self.stdout.write(
                        'Rencontre {} ajoutée'.format(rencontre.numero)
                    )

    def _downloadDataFile(self):
        """ Download csv file from ffbb """
        pass
