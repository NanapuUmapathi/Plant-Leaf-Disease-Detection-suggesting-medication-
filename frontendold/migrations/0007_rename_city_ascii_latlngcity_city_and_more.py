# Generated by Django 4.2.3 on 2023-08-04 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_latlngcity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latlngcity',
            old_name='city_ascii',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='latlngcity',
            old_name='lat',
            new_name='Latitude',
        ),
        migrations.RenameField(
            model_name='latlngcity',
            old_name='lng',
            new_name='Longitute',
        ),
    ]
