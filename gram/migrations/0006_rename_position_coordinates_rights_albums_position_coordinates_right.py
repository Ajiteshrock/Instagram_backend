# Generated by Django 4.0.1 on 2022-01-23 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0005_rename_publishe_albums_publish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albums',
            old_name='position_coordinates_rights',
            new_name='position_coordinates_right',
        ),
    ]
