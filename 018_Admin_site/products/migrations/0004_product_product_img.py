# Generated by Django 4.1.5 on 2023-01-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='defaults/clarusway.png', null=True, upload_to='product/'),
        ),
    ]