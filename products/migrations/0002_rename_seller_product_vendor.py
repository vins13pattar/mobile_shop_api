# Generated by Django 5.0.7 on 2024-07-27 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller',
            new_name='vendor',
        ),
    ]
