# Generated by Django 3.1.2 on 2020-11-07 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0018_auto_20201107_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='message',
        ),
    ]