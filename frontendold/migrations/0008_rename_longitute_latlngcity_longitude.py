# Generated by Django 4.2.3 on 2023-08-04 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_rename_city_ascii_latlngcity_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latlngcity',
            old_name='Longitute',
            new_name='Longitude',
        ),
    ]
