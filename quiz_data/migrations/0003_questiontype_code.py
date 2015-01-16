# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_data', '0002_auto_20150109_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontype',
            name='code',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
