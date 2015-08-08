# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0002_rencontre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rencontre',
            name='equipeDom',
        ),
        migrations.DeleteModel(
            name='Rencontre',
        ),
    ]
