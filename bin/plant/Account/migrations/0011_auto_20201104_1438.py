# Generated by Django 3.1.2 on 2020-11-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0010_auto_20201104_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='profile',
            field=models.ImageField(default='pic.jpg', upload_to=''),
        ),
    ]
