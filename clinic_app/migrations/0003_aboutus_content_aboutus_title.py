# Generated by Django 4.2.11 on 2024-04-10 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0002_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
