# Generated by Django 4.1.6 on 2023-05-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0009_billone_onenoq'),
    ]

    operations = [
        migrations.AddField(
            model_name='billper',
            name='nofqty',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
