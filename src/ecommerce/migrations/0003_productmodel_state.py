# Generated by Django 5.2.1 on 2025-05-16 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_productmodel_color_productmodel_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='state',
            field=models.CharField(choices=[('BR', 'BORRADOR'), ('PU', 'PUBLICADO'), ('PR', 'PRIVADO')], default='BR', max_length=2),
        ),
    ]
