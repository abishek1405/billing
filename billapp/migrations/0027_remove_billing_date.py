# Generated by Django 4.2.1 on 2023-05-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0026_alter_billing_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='date',
        ),
    ]
