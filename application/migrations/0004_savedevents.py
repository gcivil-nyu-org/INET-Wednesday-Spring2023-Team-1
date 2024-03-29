# Generated by Django 3.2.18 on 2023-04-08 19:01

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("application", "0003_eventlist_city"),
    ]

    operations = [
        migrations.CreateModel(
            name="SavedEvents",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "interestedEvents",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(null=True), null=True, size=None
                    ),
                ),
                (
                    "goingToEvents",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(null=True), null=True, size=None
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
