# Generated by Django 4.2.1 on 2023-05-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0033_remove_mymodel_field1'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytiger',
            name='name11',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
