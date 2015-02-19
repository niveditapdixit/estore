# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0005_auto_20150217_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='fullimagePath',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdescription',
            name='fullimagePath',
            field=models.CharField(max_length=100, default='test'),
            preserve_default=False,
        ),
    ]
