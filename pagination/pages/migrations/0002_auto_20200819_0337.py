# Generated by Django 3.0.5 on 2020-08-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='desc',
            field=models.CharField(max_length=200),
        ),
    ]
