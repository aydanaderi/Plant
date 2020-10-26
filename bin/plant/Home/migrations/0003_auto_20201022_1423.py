# Generated by Django 3.1.2 on 2020-10-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20201022_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='humidity_quantity',
            field=models.CharField(choices=[('low', 'low'), ('middle', 'middle'), ('high', 'high')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='plant',
            name='irrigation_quantity',
            field=models.CharField(choices=[('low', 'low'), ('middle', 'middle'), ('high', 'high')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='plant',
            name='light_quantity',
            field=models.CharField(choices=[('low', 'low'), ('middle', 'middle'), ('high', 'high')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='plant',
            name='poisonous',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='plant',
            name='sensibility',
            field=models.CharField(choices=[('low', 'low'), ('middle', 'middle'), ('high', 'high')], default='', max_length=10),
        ),
    ]