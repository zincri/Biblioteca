# Generated by Django 2.2.5 on 2019-12-12 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20191212_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='libro_id',
            new_name='libro',
        ),
        migrations.RenameField(
            model_name='detalleprestamo',
            old_name='prestador_id',
            new_name='prestador',
        ),
        migrations.RenameField(
            model_name='editorial',
            old_name='libro_id',
            new_name='libro',
        ),
        migrations.RenameField(
            model_name='libro',
            old_name='categoria_id',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='portada',
            old_name='libro_id',
            new_name='libro',
        ),
    ]
