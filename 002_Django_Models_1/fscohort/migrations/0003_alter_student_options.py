# Generated by Django 4.1.4 on 2022-12-23 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0002_alter_student_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name_plural': 'Student_List'},
        ),
    ]
