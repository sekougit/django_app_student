# Generated by Django 5.1.6 on 2025-04-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Eleve",
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
                ("prenom", models.CharField(max_length=100)),
                ("nom", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("note_francais", models.FloatField()),
                ("note_anglais", models.FloatField()),
                ("note_math", models.FloatField()),
            ],
        ),
    ]
