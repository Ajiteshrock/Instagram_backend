# Generated by Django 4.0.1 on 2022-01-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0002_alter_customuser_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='caption',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='font_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='position_coordinates_down',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='position_coordinates_left',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='position_coordinates_rights',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='position_coordinates_top',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hashtags',
            name='hashtag',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]