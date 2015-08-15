# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0009_siteconfiguration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='url_ffbb',
            field=models.CharField(verbose_name='URL du site FFBB', max_length=50),
        ),
    ]
