# Generated by Django 4.1.7 on 2023-02-27 21:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0006_alter_favoritesong_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favoritealbum",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="favoriteartist",
            old_name="user_id",
            new_name="user",
        ),
    ]