# Generated by Django 4.1.4 on 2022-12-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_alter_faculty_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='total_students',
            field=models.CharField(default='', max_length=5),
        ),
    ]
