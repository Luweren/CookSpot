# Generated by Django 3.2.1 on 2021-07-19 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CookSpot', '0024_favourite_cookfav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='meet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CookSpot.meets'),
        ),
    ]