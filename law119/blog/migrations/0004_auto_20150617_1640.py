# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150617_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_us',
            name='address',
        ),
        migrations.AddField(
            model_name='contact_us',
            name='address',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]
