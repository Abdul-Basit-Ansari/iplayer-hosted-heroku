# Generated by Django 3.2.8 on 2022-04-13 23:41

from django.db import migrations, models
import vplayer.models


class Migration(migrations.Migration):

    dependencies = [
        ('vplayer', '0005_auto_20220414_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mvideo',
            name='video',
            field=models.FileField(upload_to='myvideos', validators=[vplayer.models.validate_file_extension]),
        ),
    ]