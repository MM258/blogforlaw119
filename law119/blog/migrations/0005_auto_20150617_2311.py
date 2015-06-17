# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150617_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='myimage',
            field=models.ImageField(default='a', upload_to=b'photos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='mymap',
            field=models.ImageField(default='b', upload_to=b'photos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about_us',
            name='context',
            field=models.TextField(max_length=400),
            preserve_default=True,
        ),
    ]
