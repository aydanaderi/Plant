# Generated by Django 3.1.2 on 2020-11-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_auto_20201104_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='profile',
            field=models.FileField(default='pic.jpg', null=True, upload_to='media'),
        ),
    ]
