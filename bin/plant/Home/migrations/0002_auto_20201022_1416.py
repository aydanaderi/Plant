# Generated by Django 3.1.2 on 2020-10-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='English_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='plant',
            name='fertilizer',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='humidity',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='humidity_quantity',
            field=models.CharField(choices=[('l', 'low'), ('m', 'middle'), ('h', 'high')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='plant',
            name='irrigation',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='irrigation_quantity',
            field=models.CharField(choices=[('l', 'low'), ('m', 'middle'), ('h', 'high')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='plant',
            name='light',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='light_quantity',
            field=models.CharField(choices=[('l', 'low'), ('m', 'middle'), ('h', 'high')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='plant',
            name='poisonous',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='plant',
            name='potting',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='problems',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='sensibility',
            field=models.CharField(choices=[('l', 'low'), ('m', 'middle'), ('h', 'high')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='plant',
            name='soil',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temprature',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='plant',
            name='temprature_quantity',
            field=models.CharField(default='', max_length=500),
        ),
    ]
