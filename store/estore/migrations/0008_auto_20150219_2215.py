# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0007_auto_20150219_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='billingAddress',
            field=models.CharField(default='nivedita', max_length=1000),
            preserve_default=True,
        ),
    ]
