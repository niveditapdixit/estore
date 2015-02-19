# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0003_customer_order_orderentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.IntegerField(primary_key=True, serialize=False, max_length=20)),
                ('categoryName', models.CharField(max_length=45)),
                ('displayName', models.CharField(max_length=45)),
                ('shortDescription', models.CharField(max_length=45)),
                ('longDescription', models.CharField(max_length=45)),
                ('thumbNail', models.ImageField(blank=True, upload_to='images/', null=True)),
                ('fullImage', models.ImageField(blank=True, upload_to='images/', null=True)),
            ],
            options={
                'db_table': 'category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryChildProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('partNumber', models.CharField(max_length=45)),
                ('categoryId', models.ForeignKey(db_column='categoryId', to='estore.Category', related_name='childProductSet')),
            ],
            options={
                'db_table': 'categoryProductRelation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryXRef',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sequence', models.IntegerField(db_column='sequence')),
                ('childCategory', models.ForeignKey(db_column='child', to='estore.Category', related_name='childSet')),
                ('parentCategory', models.ForeignKey(db_column='parent', to='estore.Category', related_name='parentSet')),
            ],
            options={
                'db_table': 'categoryRelation',
                'ordering': ['sequence'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.IntegerField(primary_key=True, serialize=False, max_length=20)),
                ('partNumber', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('inventory', models.IntegerField()),
                ('salesRank', models.IntegerField(null=True)),
                ('featured', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'product',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('productId', models.ForeignKey(db_column='productId', primary_key=True, to='estore.Product', serialize=False, related_name='priceSet')),
                ('partNumber', models.CharField(max_length=45)),
                ('price', models.FloatField()),
                ('currency', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'price',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('productId', models.ForeignKey(db_column='productId', primary_key=True, to='estore.Product', serialize=False, related_name='productDescriptions')),
                ('partNumber', models.CharField(max_length=45)),
                ('displayName', models.CharField(max_length=45)),
                ('shortDescription', models.CharField(max_length=45)),
                ('longDescription', models.CharField(max_length=45)),
                ('thumbNail', models.ImageField(blank=True, upload_to='images/', null=True)),
                ('fullImage', models.ImageField(upload_to='images/')),
                ('type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'productDescription',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('childProductId', models.ForeignKey(db_column='childProductId', to='estore.Product', related_name='childProductIdSet')),
                ('parentProductId', models.ForeignKey(db_column='parentProductId', to='estore.Product', related_name='parentProductSet')),
            ],
            options={
                'db_table': 'productRelation',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categorychildproducts',
            name='childProductId',
            field=models.ForeignKey(to='estore.Product', db_column='productId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='childCategories',
            field=models.ManyToManyField(to='estore.Category', through='estore.CategoryXRef'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='childProducts',
            field=models.ManyToManyField(to='estore.Product', through='estore.CategoryChildProducts'),
            preserve_default=True,
        ),
    ]
