# Generated by Django 4.2.1 on 2023-05-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0037_partper_bnofq_partper_borr_partper_bqty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partper',
            name='bcfee',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partper',
            name='bper',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partper',
            name='btfee',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partper',
            name='btotal',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
