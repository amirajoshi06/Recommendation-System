# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
