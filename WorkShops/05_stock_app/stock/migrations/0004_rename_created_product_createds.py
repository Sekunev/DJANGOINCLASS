# Generated by Django 4.1.5 on 2023-02-01 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_brand_image_firm_image_product_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='createds',
        ),
    ]