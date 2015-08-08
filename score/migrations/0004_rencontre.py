# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0003_auto_20150808_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rencontre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('numero', models.IntegerField()),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('scoreDom', models.IntegerField()),
                ('scoreExt', models.IntegerField()),
                ('forfaitDom', models.BooleanField()),
                ('forfaitExt', models.BooleanField()),
                ('equipeDom', models.ForeignKey(to='score.Equipe', related_name='equipeDom')),
                ('equipeExt', models.ForeignKey(to='score.Equipe', related_name='equipeExt')),
            ],
        ),
    ]
