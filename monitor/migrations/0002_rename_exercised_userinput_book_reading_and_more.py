# Generated by Django 5.1.1 on 2024-10-21 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userinput",
            old_name="exercised",
            new_name="book_reading",
        ),
        migrations.RenameField(
            model_name="userinput",
            old_name="prayed",
            new_name="cultivated_relationships",
        ),
        migrations.RenameField(
            model_name="userinput",
            old_name="satisfied",
            new_name="exercised_or_played",
        ),
        migrations.AddField(
            model_name="userinput",
            name="healthy_eating",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userinput",
            name="masturbated",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userinput",
            name="prayed_for_world_peace",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userinput",
            name="studying_machine_learning",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userinput",
            name="wasted_time",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="userinput",
            name="woke_up_at_5am",
            field=models.BooleanField(default=False),
        ),
    ]