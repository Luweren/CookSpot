# Generated by Django 3.2.5 on 2021-07-04 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CookSpot', '0017_auto_20210701_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='meet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CookSpot.meets'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CookSpot.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
