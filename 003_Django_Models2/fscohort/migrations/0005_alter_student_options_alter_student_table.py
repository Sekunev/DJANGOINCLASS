# Generated by Django 4.1.4 on 2022-12-22 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0004_student_about_student_avatar_student_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('-first_name',), 'verbose_name': 'Öğrenci', 'verbose_name_plural': 'Öğrenciler'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='Ögrenciler',
        ),
    ]