# Generated by Django 2.2.5 on 2019-12-12 04:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('inicio', '0002_auto_20191211_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('activo', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('anio_publicacion', models.CharField(blank=True, max_length=10, null=True)),
                ('estado_prestado', models.BooleanField(blank=True, default=False, null=True)),
                ('activo', models.BooleanField(blank=True, default=True, null=True)),
                ('categoria_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicio.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='prestador',
            name='activo',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='prestador',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Portada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('activo', models.BooleanField(blank=True, default=True, null=True)),
                ('libro_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicio.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(blank=True, default=True, null=True)),
                ('libro_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicio.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePrestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_vencimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('activo', models.BooleanField(blank=True, default=True, null=True)),
                ('libro_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicio.Libro')),
                ('prestador_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inicio.Prestador')),
            ],
        ),
    ]
