# Generated by Django 4.0.4 on 2022-08-19 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shareboard',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
