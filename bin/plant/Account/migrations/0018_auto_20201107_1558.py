# Generated by Django 3.1.2 on 2020-11-07 15:58

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0017_auto_20201107_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='message',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, size=None),
        ),
    ]
