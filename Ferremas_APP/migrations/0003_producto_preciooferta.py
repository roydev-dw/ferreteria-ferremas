# Generated by Django 5.0.5 on 2024-05-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferremas_APP', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precioOferta',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]