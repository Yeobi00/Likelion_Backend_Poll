# Generated by Django 5.0.4 on 2024-05-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('agree', models.PositiveIntegerField(default=0)),
                ('disagree', models.PositiveIntegerField(default=0)),
                ('agreeRate', models.FloatField(default=0.0)),
                ('disagreeRate', models.FloatField(default=0.0)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
