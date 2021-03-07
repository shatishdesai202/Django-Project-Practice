# Generated by Django 3.0.5 on 2020-08-13 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelinheritance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='like',
            name='user_liked',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='modelinheritance.Page'),
            preserve_default=False,
        ),
    ]
