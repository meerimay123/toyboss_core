# Generated by Django 5.1.2 on 2024-10-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir_kolbass', '0007_recipe_composition'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='composition',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
