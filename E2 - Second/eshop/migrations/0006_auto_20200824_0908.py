# Generated by Django 3.0.5 on 2020-08-24 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_placeorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placeorder',
            old_name='first_name',
            new_name='firstname',
        ),
    ]
