# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(max_length=300),
            preserve_default=True,
        ),
    ]
