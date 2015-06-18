# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_case_case_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='my_map',
            field=models.ForeignKey(default='2', to='blog.Picture'),
            preserve_default=False,
        ),
    ]
