# Generated by Django 5.0.4 on 2024-05-16 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='agreeRate',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='disagreeRate',
        ),
    ]
