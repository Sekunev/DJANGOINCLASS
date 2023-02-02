# Generated by Django 4.1.5 on 2023-02-01 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_alter_purchases_price_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='firm',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
