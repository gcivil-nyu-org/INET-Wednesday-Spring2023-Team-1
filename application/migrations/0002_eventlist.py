# Generated by Django 3.2.18 on 2023-04-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventList",
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
                ("event_name", models.CharField(max_length=300)),
                ("start_date", models.DateField()),
                ("start_time", models.CharField(max_length=8)),
                ("venue_name", models.CharField(max_length=300)),
                ("img_url", models.CharField(max_length=300)),
            ],
        ),
    ]