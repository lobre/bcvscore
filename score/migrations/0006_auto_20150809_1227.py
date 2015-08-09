# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0005_auto_20150809_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rencontre',
            name='equipeDom',
            field=models.ForeignKey(verbose_name='Equipe Domicile', to='score.Equipe', related_name='rencontreDom'),
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='equipeExt',
            field=models.ForeignKey(verbose_name='Equipe Exterieur', to='score.Equipe', related_name='rencontreExt'),
        ),
    ]
