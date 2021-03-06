# Generated by Django 3.2.8 on 2022-04-19 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vplayer.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vplayer', '0012_auto_20220419_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maudio',
            name='cover',
            field=models.ImageField(blank=True, default='', null=True, upload_to='mycover', validators=[vplayer.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='maudio',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='mvideo',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Acomment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vplayer.maudio')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vplayer.acomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
