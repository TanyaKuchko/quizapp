# Generated by Django 4.2.1 on 2023-05-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='logo',
            field=models.ImageField(blank=True, upload_to='quizes/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, upload_to='teams/'),
        ),
    ]