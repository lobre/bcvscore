# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0008_auto_20150809_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('login', models.CharField(max_length=7, verbose_name='Identifiant')),
                ('password', models.CharField(max_length=8, verbose_name='Mot de passe')),
                ('url_ffbb', models.CharField(max_length=50, verbose_name='Url du site FFBB')),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
