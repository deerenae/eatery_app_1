# Generated by Django 3.0.7 on 2020-07-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatery_backend', '0003_auto_20200708_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='carry_out',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='dine_in',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]