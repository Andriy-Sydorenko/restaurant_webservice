# Generated by Django 4.2.3 on 2023-07-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0004_alter_cook_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(default=0),
        ),
    ]
