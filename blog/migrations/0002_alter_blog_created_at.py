# Generated by Django 5.0.6 on 2024-06-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="created_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата создания"
            ),
        ),
    ]
