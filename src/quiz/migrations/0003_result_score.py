# Generated by Django 4.2.2 on 2023-06-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0002_category_create_datetime_category_last_update_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]
