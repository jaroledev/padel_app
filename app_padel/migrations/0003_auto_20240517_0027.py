# Generated by Django 2.2.28 on 2024-05-17 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_padel', '0002_auto_20240517_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='admin_id',
            new_name='admin_id_id',
        ),
    ]