# Generated by Django 5.1.5 on 2025-02-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0005_assessmentquestion_alter_assessment_score_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
