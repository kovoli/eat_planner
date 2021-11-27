# Generated by Django 3.2.9 on 2021-11-27 19:40

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0004_recept_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recept',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='recept_images'),
        ),
    ]