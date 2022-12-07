# Generated by Django 4.1.3 on 2022-12-06 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_birthdate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.AddField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(default=False),
        ),
    ]