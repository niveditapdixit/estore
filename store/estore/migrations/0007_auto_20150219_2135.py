# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0006_auto_20150217_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='emailId',
            field=models.CharField(default='nivedita@infosys.com', max_length=45),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='Infy2015', max_length=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productdescription',
            name='fullImage',
            field=models.ImageField(upload_to='estore/prodimages/', blank=True, null=True),
            preserve_default=True,
        ),
    ]
