# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('division', models.ForeignKey(verbose_name='Division', to='score.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('equipes', models.ManyToManyField(to='score.Equipe')),
                ('user', models.OneToOneField(verbose_name='Utilisateur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rencontre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('scoreDom', models.IntegerField(verbose_name='Score Domicile', blank=True, null=True)),
                ('scoreExt', models.IntegerField(verbose_name='Score Exterieur', blank=True, null=True)),
                ('forfaitDom', models.BooleanField(verbose_name='Forfait Domicile', default=False)),
                ('forfaitExt', models.BooleanField(verbose_name='Forfait Exterieur', default=False)),
                ('equipeDom', models.ForeignKey(verbose_name='Equipe Domicile', related_name='rencontreDom', to='score.Equipe')),
                ('equipeExt', models.ForeignKey(verbose_name='Equipe Exterieur', related_name='rencontreExt', to='score.Equipe')),
            ],
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('login', models.CharField(verbose_name='Identifiant', max_length=7)),
                ('password', models.CharField(verbose_name='Mot de passe', max_length=8)),
                ('username', models.CharField(verbose_name='Nom utilisateur', max_length=20)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
