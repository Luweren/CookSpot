# Generated by Django 3.2.3 on 2021-06-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookSpot', '0006_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
