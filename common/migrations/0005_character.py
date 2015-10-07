# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20151002_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_en', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField(default=b'', blank=True)),
                ('episodes', models.ManyToManyField(to='common.Episode')),
            ],
        ),
    ]
