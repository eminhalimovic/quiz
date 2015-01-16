# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_data', '0003_questiontype_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=1024),
            preserve_default=True,
        ),
    ]
