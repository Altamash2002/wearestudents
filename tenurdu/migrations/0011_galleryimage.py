# Generated by Django 5.0.1 on 2024-02-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenurdu', '0010_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.ImageField(upload_to='gallery_images/')),
            ],
        ),
    ]
