# Generated by Django 3.1 on 2020-11-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_televisores'),
    ]

    operations = [
        migrations.AddField(
            model_name='especificaciones',
            name='recomendacion',
            field=models.TextField(default=6),
            preserve_default=False,
        ),
    ]