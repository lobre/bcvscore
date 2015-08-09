# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('score', '0004_rencontre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('equipes', models.ManyToManyField(to='score.Equipe')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='equipeDom',
            field=models.ForeignKey(related_name='equipeDom', to='score.Equipe', verbose_name='Equipe Domicile'),
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='equipeExt',
            field=models.ForeignKey(related_name='equipeExt', to='score.Equipe', verbose_name='Equipe Exterieur'),
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='forfaitDom',
            field=models.BooleanField(verbose_name='Forfait Domicile', default=False),
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='forfaitExt',
            field=models.BooleanField(verbose_name='Forfait Exterieur', default=False),
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='scoreDom',
            field=models.IntegerField(null=True, verbose_name='Score Domicile'),
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='scoreExt',
            field=models.IntegerField(null=True, verbose_name='Score Exterieur'),
        ),
    ]
