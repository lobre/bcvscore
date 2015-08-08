# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rencontre',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('scoreDom', models.IntegerField()),
                ('scoreExt', models.IntegerField()),
                ('forfaitDom', models.BooleanField()),
                ('forfaitExt', models.BooleanField()),
                ('equipeDom', models.ForeignKey(to='score.Equipe')),
            ],
        ),
    ]
