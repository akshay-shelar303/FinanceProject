# Generated by Django 4.0.1 on 2022-01-18 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BankDetails",
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
                ("account_holder_name", models.CharField(max_length=100)),
                ("account_no", models.IntegerField()),
                ("bank_name", models.CharField(max_length=100)),
                ("branch_name", models.CharField(max_length=100)),
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("SAVING", "Saving"),
                            ("CURRENT", "Current"),
                            ("SALARIED", "Salaried"),
                        ],
                        max_length=40,
                    ),
                ),
                ("ifsc_code", models.CharField(max_length=50)),
                ("micr_code", models.CharField(max_length=100)),
                (
                    "customer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Customer.customer",
                    ),
                ),
            ],
        ),
    ]
