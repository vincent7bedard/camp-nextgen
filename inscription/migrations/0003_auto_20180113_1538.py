# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0002_enfant_a_deja_paye'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfant',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Enfant',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
    ]
