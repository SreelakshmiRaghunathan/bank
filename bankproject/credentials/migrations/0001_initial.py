# Generated by Django 4.1 on 2023-10-03 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("state", models.CharField(max_length=50)),
                ("district", models.CharField(max_length=50)),
                ("branch", models.CharField(max_length=50)),
                ("account", models.CharField(max_length=50)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]