# Generated by Django 5.1.2 on 2024-10-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir_kolbass', '0005_alter_socialmediacontact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1, verbose_name='описание'),
            preserve_default=False,
        ),
    ]
