# Generated by Django 4.2.1 on 2023-05-14 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0042_alter_partper_bproduct_alter_partper_datt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partper',
            name='bcfee',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='partper',
            name='bper',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='partper',
            name='btfee',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='partper',
            name='btotal',
            field=models.CharField(max_length=1000),
        ),
    ]
