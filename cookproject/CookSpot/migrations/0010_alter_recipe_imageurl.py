# Generated by Django 3.2.1 on 2021-06-12 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookSpot', '0009_auto_20210612_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='imageURL',
            field=models.URLField(),
        ),
    ]
