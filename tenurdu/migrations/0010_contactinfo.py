# Generated by Django 5.0.2 on 2024-02-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenurdu', '0009_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
