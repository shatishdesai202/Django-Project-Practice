# Generated by Django 3.0.5 on 2020-08-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0006_auto_20200824_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='customer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placeorder',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eshop.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placeorder',
            name='qty',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
