# Generated by Django 5.1.5 on 2025-01-28 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("therapist", "0002_diaryentry"),
    ]

    operations = [
        migrations.AddField(
            model_name="diaryentry",
            name="title",
            field=models.CharField(default="Untitled", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="diaryentry",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="diaryentry",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
