# Generated by Django 3.1.2 on 2020-10-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20201019_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
