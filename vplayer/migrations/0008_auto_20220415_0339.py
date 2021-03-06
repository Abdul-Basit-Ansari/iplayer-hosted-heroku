# Generated by Django 3.2.8 on 2022-04-14 22:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vplayer', '0007_auto_20220414_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maudio',
            name='audio',
            field=models.FileField(upload_to='myaudio', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'ogg', 'wav'])]),
        ),
        migrations.AlterField(
            model_name='mvideo',
            name='video',
            field=models.FileField(upload_to='myvideos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'wmv', 'avi', 'mkv', 'flv', 'swf', 'webm', 'f4v', 'swf'])]),
        ),
    ]
