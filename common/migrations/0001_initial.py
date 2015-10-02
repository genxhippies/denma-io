# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.SmallIntegerField()),
                ('subtitle', models.CharField(max_length=1024)),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
