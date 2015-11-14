# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicLOL', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summoner',
            name='id',
        ),
        migrations.AlterField(
            model_name='summoner',
            name='summoner_id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
