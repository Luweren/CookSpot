# Generated by Django 3.2.3 on 2021-06-02 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CookSpot', '0002_auto_20210602_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]