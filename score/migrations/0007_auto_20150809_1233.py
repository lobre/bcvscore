# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0006_auto_20150809_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rencontre',
            name='scoreDom',
            field=models.IntegerField(blank=True, null=True, verbose_name='Score Domicile'),
        ),
        migrations.AlterField(
            model_name='rencontre',
            name='scoreExt',
            field=models.IntegerField(blank=True, null=True, verbose_name='Score Exterieur'),
        ),
    ]
