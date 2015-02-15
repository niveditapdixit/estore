# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
       
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.IntegerField(serialize=False, primary_key=True, max_length=20)),
                ('firstName', models.CharField(max_length=45)),
                ('lastName', models.CharField(max_length=45)),
                ('shippingAddress', models.CharField(max_length=1000)),
                ('billingAddress', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'customer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.IntegerField(serialize=False, primary_key=True, max_length=20)),
                ('totalPrice', models.FloatField()),
                ('totalDiscount', models.FloatField()),
                ('totalTax', models.FloatField()),
                ('customer', models.ForeignKey(db_column='customerId', to='estore.Customer', related_name='customerSet')),
            ],
            options={
                'db_table': 'order',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderEntry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('productId', models.IntegerField(max_length=20)),
                ('partNumber', models.CharField(max_length=45)),
                ('quantity', models.IntegerField(max_length=20)),
                ('totalPrice', models.FloatField()),
                ('totalDiscount', models.FloatField()),
                ('totalTax', models.FloatField()),
                ('sequence', models.IntegerField(db_column='sequence')),
                ('orderId', models.ForeignKey(db_column='orderId', to='estore.Order', related_name='orderSet')),
            ],
            options={
                'db_table': 'orderEntry',
            },
            bases=(models.Model,),
        ),
    ]
