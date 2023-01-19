# Generated by Django 4.1.5 on 2023-01-17 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveIntegerField(choices=[(1, 'SELLER'), (2, 'CUSTOMER')])),
                ('display_name', models.CharField(blank=True, max_length=30, null=True)),
                ('avatar', models.ImageField(default='avatar.png', upload_to='users')),
                ('bio', models.TextField(blank=True, null=True)),
                ('cards', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.card')),
                ('favorites', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.favorites')),
                ('sell_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
