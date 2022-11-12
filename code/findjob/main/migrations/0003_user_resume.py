# Generated by Django 4.1.2 on 2022-11-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_dreamreal_email_alter_dreamreal_pid"),
    ]

    operations = [
        migrations.CreateModel(
            name="user_resume",
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
                ("pid", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                ("firstname", models.CharField(max_length=50)),
                ("user_resumestyle", models.CharField(max_length=50)),
                ("user_skill", models.CharField(max_length=200)),
                ("user_selfintroduction", models.CharField(max_length=2000)),
                ("user_education", models.CharField(max_length=200)),
                ("user_experience", models.CharField(max_length=2000)),
            ],
            options={
                "db_table": "user_resume",
            },
        ),
    ]