# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwardNominee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=55)),
                ('image', models.CharField(max_length=30)),
                ('votes', models.IntegerField()),
            ],
        ),
    ]
