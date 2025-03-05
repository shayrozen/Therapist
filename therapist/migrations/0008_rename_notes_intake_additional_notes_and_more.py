# Generated by Django 5.1.5 on 2025-02-27 08:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0007_remove_assessment_assessment_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intake',
            old_name='notes',
            new_name='additional_notes',
        ),
        migrations.AddField(
            model_name='intake',
            name='addictions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='body_pain',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='country_of_birth',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='current_occupation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='intake',
            name='emotional_physical_issues',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='family_background',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='hobbies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='life_turning_points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='marital_status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='medications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='nutrition_habits',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='past_treatments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='physical_activity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='reason_for_therapy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='religious_beliefs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='repeating_patterns',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='smoking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='intake',
            name='strengths_and_resources',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intake',
            name='substance_use',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='intake',
            name='therapy_goals',
            field=models.TextField(blank=True, null=True),
        ),
    ]
