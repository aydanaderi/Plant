# Generated by Django 3.1.2 on 2020-10-17 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_remove_information_random'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='time',
        ),
    ]
