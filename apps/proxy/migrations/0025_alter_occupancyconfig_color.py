# Generated by Django 4.2.6 on 2024-01-10 01:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proxy", "0024_occupancyconfig_color_occupancyconfig_remark_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="occupancyconfig",
            name="color",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "empty"),
                    ("is-info", "is-info"),
                    ("is-link", "is-link"),
                    ("is-primary", "is-primary"),
                    ("is-danger", "is-danger"),
                    ("is-warning", "is-warning"),
                    ("is-success", "is-success"),
                ],
                default="",
                max_length=32,
                verbose_name="颜色",
            ),
        ),
    ]
