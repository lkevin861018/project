# Generated by Django 4.1.2 on 2022-11-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_companyacc_jobs_salary"),
    ]

    operations = [
        migrations.AddField(
            model_name="companyacc_jobs",
            name="address",
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
