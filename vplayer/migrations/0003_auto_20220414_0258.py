# Generated by Django 3.2.8 on 2022-04-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vplayer', '0002_auto_20220414_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='maudio',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mvideo',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]