# Generated by Django 4.0.1 on 2022-01-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]