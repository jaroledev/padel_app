# Generated by Django 4.2.5 on 2024-06-05 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_padel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='admin_id',
        ),
    ]
