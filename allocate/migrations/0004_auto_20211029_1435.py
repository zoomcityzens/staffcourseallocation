# Generated by Django 3.2.8 on 2021-10-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocate', '0003_auto_20211029_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='course',
            name='facilitator',
        ),
        migrations.RemoveField(
            model_name='course',
            name='location',
        ),
        migrations.AddField(
            model_name='allocation',
            name='duration',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='allocation',
            name='facilitator',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='allocation',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]