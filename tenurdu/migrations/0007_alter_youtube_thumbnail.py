# Generated by Django 5.0.2 on 2024-02-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenurdu', '0006_alter_youtube_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
