# Generated by Django 3.0.5 on 2020-08-26 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0012_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='coms',
            new_name='comment',
        ),
    ]
