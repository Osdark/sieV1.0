# Generated by Django 2.0.5 on 2018-05-06 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0003_auto_20180504_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=120, null=True)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
            options={
                'verbose_name': 'Peticion',
                'verbose_name_plural': 'Peticiones',
            },
        ),
    ]