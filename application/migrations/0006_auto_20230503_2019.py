# Generated by Django 3.2.18 on 2023-05-04 00:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0005_reports"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprompts",
            name="response1_id",
            field=models.CharField(default="null", max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprompts",
            name="response2_id",
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprompts",
            name="response3_id",
            field=models.CharField(default="null", max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprompts",
            name="response4_id",
            field=models.CharField(default="null", max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprompts",
            name="response5_id",
            field=models.CharField(default="null", max_length=300),
            preserve_default=False,
        ),
    ]
