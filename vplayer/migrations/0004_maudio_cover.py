# Generated by Django 3.2.8 on 2022-04-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vplayer', '0003_auto_20220414_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='maudio',
            name='cover',
            field=models.ImageField(default=1, upload_to='mycover'),
            preserve_default=False,
        ),
    ]
