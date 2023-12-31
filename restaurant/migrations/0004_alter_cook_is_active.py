# Generated by Django 4.2.3 on 2023-07-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "restaurant",
            "0003_alter_cook_is_active_alter_cook_years_of_experience_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
