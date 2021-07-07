# Generated by Django 3.2.5 on 2021-07-04 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CookSpot', '0019_auto_20210704_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='cook',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='favcook', to='auth.user'),
            preserve_default=False,
        ),
    ]
