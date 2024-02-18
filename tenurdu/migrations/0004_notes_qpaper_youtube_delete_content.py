# Generated by Django 5.0.2 on 2024-02-15 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenurdu', '0003_content_cname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('notes', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenurdu.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Qpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('qpaper', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenurdu.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('youtube_link', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenurdu.subject')),
            ],
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
