# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150617_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='context',
            field=models.CharField(default='nuli', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='company',
            field=models.CharField(default='mtn-sh', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(default='975474724@qq.com', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='name',
            field=models.CharField(default='hong wei', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='website',
            field=models.URLField(default='mtn-sh.com'),
            preserve_default=False,
        ),
    ]
