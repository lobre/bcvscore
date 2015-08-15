# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0010_auto_20150815_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='nom',
            field=models.CharField(max_length=30),
        ),
    ]
