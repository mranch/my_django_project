# Generated by Django 4.1.7 on 2023-07-07 15:53

import autoslug.fields
from django.db import migrations
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=recipes.models.custom_slugify, unique=True),
        ),
    ]