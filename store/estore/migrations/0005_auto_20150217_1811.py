# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0004_auto_20150217_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdescription',
            name='fullImage',
            field=models.ImageField(upload_to='images/', null=True, blank=True),
            preserve_default=True,
        ),
    ]
