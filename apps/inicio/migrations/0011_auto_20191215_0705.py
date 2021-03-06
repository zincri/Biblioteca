# Generated by Django 2.2.5 on 2019-12-15 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0010_auto_20191215_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleprestamo',
            name='libro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libro', to='inicio.Libro'),
        ),
        migrations.AlterField(
            model_name='detalleprestamo',
            name='prestador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prestador', to='inicio.Prestador'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='inicio.Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='inicio.Categoria', verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editorial', to='inicio.Editorial'),
        ),
        migrations.AlterField(
            model_name='portada',
            name='libro',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portada', to='inicio.Libro'),
        ),
    ]
