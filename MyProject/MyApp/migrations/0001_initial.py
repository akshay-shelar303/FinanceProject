# Generated by Django 4.0.1 on 2022-01-18 06:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquiry",
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
                ("full_name", models.CharField(max_length=30)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "mobile",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("city", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="LoanDetails",
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
                ("full_name", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=32,
                    ),
                ),
                ("dob", models.DateField()),
                (
                    "mobile",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("pan_number", models.CharField(max_length=32)),
                ("required_loan", models.IntegerField()),
                ("cibil_score", models.IntegerField(default=None)),
                ("is_eligible", models.BooleanField(default=False)),
            ],
        ),
    ]
