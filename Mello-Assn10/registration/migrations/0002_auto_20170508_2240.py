# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='card_type',
            field=models.CharField(choices=[('MC', 'Mastercard'), ('V', 'Visa'), ('AE', 'American Express')], max_length=16),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='meals',
            field=models.CharField(choices=[('mealpack', 'Meal Pack'), ('dinnerday2', 'Dinner Day 2')], max_length=30),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='session1',
            field=models.CharField(choices=[('Workshop_A', 'Workshop A'), ('Workshop_B', 'Workshop B'), ('Workshop_C', 'Workshop C')], max_length=35),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='session2',
            field=models.CharField(choices=[('Workshop_D', 'Workshop D'), ('Workshop_E', 'Workshop E'), ('Workshop_F', 'Workshop F')], max_length=35),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='session3',
            field=models.CharField(choices=[('Workshop_G', 'Workshop G'), ('Workshop_H', 'Workshop H'), ('Workshop_I', 'Workshop I')], max_length=35),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MS', 'Ms.'), ('MRS', 'Mrs.'), ('SR', 'Sr.'), ('JR', 'Jr.')], max_length=3),
        ),
    ]
