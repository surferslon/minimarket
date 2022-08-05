# Generated by Django 4.1 on 2022-08-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=64)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("count", models.PositiveIntegerField()),
                ("categories", models.ManyToManyField(to="products.category")),
            ],
        ),
    ]
