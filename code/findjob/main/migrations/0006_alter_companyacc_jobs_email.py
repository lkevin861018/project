# Generated by Django 4.1.2 on 2022-11-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_companyacc_jobs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyacc_jobs",
            name="email",
            field=models.CharField(max_length=50),
        ),
    ]
