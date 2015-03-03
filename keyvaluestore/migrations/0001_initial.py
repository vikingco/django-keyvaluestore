# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValueStore',
            fields=[
                ('key', models.CharField(max_length=200, unique=True, serialize=False, primary_key=True, db_index=True)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Key Value pair',
                'verbose_name_plural': 'Key Value pairs',
            },
            bases=(models.Model,),
        ),
    ]
