# Generated by Django 4.1.2 on 2022-11-24 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_shop_pid"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="shop",
            table="shophistory",
        ),
    ]
