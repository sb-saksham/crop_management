# Generated by Django 4.0.4 on 2022-05-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop_stats', '0002_cropstats_crop_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropstats',
            name='crop_health',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
