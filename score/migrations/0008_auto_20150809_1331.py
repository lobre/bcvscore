# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0007_auto_20150809_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='division',
            field=models.ForeignKey(verbose_name='Division', to='score.Division'),
        ),
    ]
