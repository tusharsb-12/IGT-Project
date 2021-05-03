# Generated by Django 3.2 on 2021-05-02 17:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weighted_means', '0002_centroids01'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centroids11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Centroids 2011',
            },
        ),
        migrations.AlterModelOptions(
            name='centroids01',
            options={'verbose_name_plural': 'Centroids 2001'},
        ),
    ]
