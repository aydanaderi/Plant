# Generated by Django 3.1.2 on 2020-10-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_remove_information_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='newpassword',
            field=models.CharField(default='', max_length=100),
        ),
    ]
