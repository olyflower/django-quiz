# Generated by Django 4.2.2 on 2023-06-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0003_result_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
    ]