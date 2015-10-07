# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_character'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='episodes',
        ),
        migrations.AddField(
            model_name='episode',
            name='characters',
            field=models.ManyToManyField(to='common.Character', blank=True),
        ),
    ]
