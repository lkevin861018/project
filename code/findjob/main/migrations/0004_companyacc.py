# Generated by Django 4.1.2 on 2022-11-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_user_resume"),
    ]

    operations = [
        migrations.CreateModel(
            name="companyacc",
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
                ("companyname", models.CharField(max_length=50)),
                ("pid", models.CharField(max_length=50, unique=True)),
                ("email", models.CharField(max_length=50, unique=True)),
                ("passwd", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "campanyacc",
            },
        ),
    ]
