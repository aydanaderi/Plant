# Generated by Django 3.1.2 on 2020-11-07 16:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0021_auto_20201107_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='message',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
    ]
