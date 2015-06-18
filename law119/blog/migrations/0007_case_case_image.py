# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150618_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='case_image',
            field=models.ForeignKey(default='1', to='blog.Picture'),
            preserve_default=False,
        ),
    ]
