# Generated by Django 3.2.1 on 2021-07-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CookSpot', '0027_remove_recipe_ingredients_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='measurement',
            field=models.CharField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]