# Generated by Django 4.1.3 on 2022-12-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="added_by",
            field=models.EmailField(default="teste1@email.com", max_length=254),
            preserve_default=False,
        ),
    ]
