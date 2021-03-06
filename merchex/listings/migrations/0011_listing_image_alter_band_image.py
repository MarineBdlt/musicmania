# Generated by Django 4.0 on 2022-01-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_band_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='assets/img/intrument.png', upload_to='assets/img/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(upload_to='assets/img/'),
        ),
    ]
