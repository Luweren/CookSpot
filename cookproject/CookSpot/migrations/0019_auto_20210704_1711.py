# Generated by Django 3.2.5 on 2021-07-04 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CookSpot', '0018_auto_20210704_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='cook',
        ),
        migrations.AddField(
            model_name='favourite',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CookSpot.recipe'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
