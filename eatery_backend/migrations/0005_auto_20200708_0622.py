# Generated by Django 3.0.7 on 2020-07-08 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eatery_backend', '0004_auto_20200708_0617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='delivery',
            new_name='has_online_delivery',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='dine_in',
            new_name='has_table_booking',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='image',
            new_name='menu_url',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='phone_number',
            new_name='phone_numbers',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='menu',
            new_name='thumb',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='website',
            new_name='url',
        ),
    ]
