# Generated by Django 4.1.7 on 2023-02-27 17:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="favorites",
            new_name="Favorite",
        ),
    ]
