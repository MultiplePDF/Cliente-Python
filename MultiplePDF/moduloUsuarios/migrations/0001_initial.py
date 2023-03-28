# Generated by Django 4.1 on 2023-03-26 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("user", models.CharField(max_length=20)),
                ("name_user", models.CharField(max_length=85)),
                ("password", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=40)),
            ],
        ),
    ]
