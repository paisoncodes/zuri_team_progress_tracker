# Generated by Django 3.2.8 on 2021-11-01 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_intern_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="intern",
            options={"ordering": ("-created_at",)},
        ),
    ]
