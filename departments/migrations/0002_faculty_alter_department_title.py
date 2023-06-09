# Generated by Django 4.1.4 on 2022-12-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images')),
                ('job_profile', models.CharField(default='', max_length=100)),
                ('area_of_interest', models.CharField(default='', max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email_id', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
