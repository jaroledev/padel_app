# Generated by Django 4.2.5 on 2024-05-20 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_padel', '0004_alter_club_id_alter_dimensiones_id_alter_pista_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallesClub',
            fields=[
                ('club', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app_padel.club')),
                ('ubicacion', models.CharField(max_length=255)),
                ('descripcion_larga', models.TextField()),
                ('numero_pistas', models.IntegerField()),
                ('imagen_principal', models.TextField()),
                ('imagen_secundaria', models.TextField()),
            ],
        ),
    ]
