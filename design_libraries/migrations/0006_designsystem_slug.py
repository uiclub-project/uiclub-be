# Generated by Django 4.2.17 on 2025-02-14 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('design_libraries', '0005_designsystem_thumbnail_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='designsystem',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
