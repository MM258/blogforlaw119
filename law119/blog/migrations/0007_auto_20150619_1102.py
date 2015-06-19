# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150619_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='context',
            field=models.TextField(max_length=4000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='case',
            name='case_content',
            field=models.CharField(max_length=3000),
            preserve_default=True,
        ),
    ]
