# Generated by Django 4.2.1 on 2023-05-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Programming_language",
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
                (
                    "name_city",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Язык програмирования"
                    ),
                ),
                ("slug", models.CharField(blank=True, max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Язык програмирования",
                "verbose_name_plural": "Языки програмирования",
            },
        ),
        migrations.AlterModelOptions(
            name="city",
            options={
                "verbose_name": "Название населенного пункта",
                "verbose_name_plural": "Название населенных пунктов",
            },
        ),
        migrations.AlterField(
            model_name="city",
            name="name_city",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="Название населенного пункта"
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="slug",
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]