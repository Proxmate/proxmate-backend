# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxmate', '0005_auto_20151001_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='plan_status',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
