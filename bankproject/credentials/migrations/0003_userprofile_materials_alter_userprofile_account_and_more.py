# Generated by Django 4.1 on 2023-10-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("credentials", "0002_remove_userprofile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="materials",
            field=models.CharField(default="Creditcard", max_length=30),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="account",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="age",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="branch",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="district",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="state",
            field=models.CharField(max_length=30),
        ),
    ]
