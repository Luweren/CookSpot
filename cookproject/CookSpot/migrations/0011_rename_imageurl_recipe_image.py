# Generated by Django 3.2.1 on 2021-06-12 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CookSpot', '0010_alter_recipe_imageurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='imageURL',
            new_name='image',
        ),
    ]