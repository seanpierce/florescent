# Generated by Django 3.0.7 on 2021-11-04 03:41

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=1000, storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to=''),
        ),
    ]
