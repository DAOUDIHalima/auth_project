# Generated by Django 4.0.8 on 2023-08-20 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_info_ant_professionneles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systematique',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]