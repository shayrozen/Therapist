# Generated by Django 5.1.5 on 2025-01-23 14:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("therapist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiaryEntry",
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
                ("date", models.DateField(auto_now_add=True)),
                ("content", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="diary_entries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
