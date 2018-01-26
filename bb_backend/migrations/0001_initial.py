# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand_name', models.CharField(max_length=50)),
                ('brand_logo', models.ImageField(upload_to='brandlogo/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categories_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colour', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='productimage/')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(to='bb_backend.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=50)),
                ('product_price', models.FloatField(default=None, null=True, blank=True)),
                ('product_description', models.CharField(max_length=100)),
                ('product_brand', models.ForeignKey(to='bb_backend.Brand')),
                ('product_colour', models.ManyToManyField(to='bb_backend.Colour')),
                ('product_image', models.ManyToManyField(to='bb_backend.Image')),
                ('product_item', models.ForeignKey(to='bb_backend.Item')),
            ],
        ),
    ]
