from django.core.management.base import BaseCommand
from django.conf import settings
from score.models import Division, Equipe, Rencontre, SiteConfiguration
import csv
import datetime
import requests


class Command(BaseCommand):
    help = 'Commande pour importer les données'

    def handle(self, *args, **options):
        if(self._downloadDataFile()):
            self._importInDjango()
        else:
            print('Impossible de télécharger le CSV')

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
                    equipeDom=equipeDom,
                    equipeExt=equipeExt,
                    defaults={
                        'date': date,
                        'heure': heure,
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
        config = SiteConfiguration.objects.get()

        with requests.Session() as s:
            # Authentication
            data = {
                'identificationBean.identifiant': '{}'.format(config.login),
                'identificationBean.mdp': '{}'.format(config.password),
                'userName': '{}'.format(config.username)
            }
            url = 'http://extranet.ffbb.com/fbi/identification.do'
            s.post(url, data=data)

            # Create filters
            params = (
                ('action', 'executeCsv'),
                ('rechercherRencontreSaisieResultatBean.idDivision', ''),
                ('rechercherRencontreSaisieResultatBean.rechercherEquipe2', 'O'),
                ('rechercherRencontreSaisieResultatBean.dateDebutRencontre', ''),
                ('rechercherRencontreSaisieResultatBean.dateFinRencontre', ''),
                ('rechercherRencontreSaisieResultatBean.idPoule', ''),
                ('rechercherRencontreSaisieResultatBean.numeroEquipe', ''),
            )

            # Get Csv file
            url = 'http://extranet.ffbb.com/fbi/rechercherCompetitionRencontre.do'
            response = s.get(url, params=params)

            if(response.headers['content-type'] != 'application/ms-excel;charset=UTF-8'):
                return False

            # Create the file
            if response.status_code == 200:
                with open(settings.DATA_PATH, 'wb') as f:
                    for chunk in response:
                        f.write(chunk)

        return True
