# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150617_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=b'photos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='contact_us',
            name='mymap',
        ),
        migrations.AddField(
            model_name='case',
            name='anli',
            field=models.CharField(default='q', max_length=1, choices=[(b'J', b'jinji'), (b'X', b'xingshi')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about_us',
            name='myimage',
            field=models.ForeignKey(to='blog.Picture'),
            preserve_default=True,
        ),
    ]
