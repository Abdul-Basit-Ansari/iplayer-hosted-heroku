# Generated by Django 3.2.8 on 2022-04-13 23:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vplayer', '0004_maudio_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maudio',
            name='audio',
            field=models.FileField(upload_to='myaudio', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'ogg'])]),
        ),
        migrations.AlterField(
            model_name='maudio',
            name='cover',
            field=models.ImageField(upload_to='mycover', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'gif'])]),
        ),
        migrations.AlterField(
            model_name='mvideo',
            name='video',
            field=models.FileField(upload_to='myvideos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'mpg', 'avi', 'wmv', 'mpeg2', 'mpeg4'])]),
        ),
    ]
