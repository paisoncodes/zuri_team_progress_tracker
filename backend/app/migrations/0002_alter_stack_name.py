# Generated by Django 3.2.8 on 2021-10-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stack',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
