# Generated by Django 5.0.6 on 2024-07-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blog_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото продукта",
                null=True,
                upload_to="media/picture_blog/",
                verbose_name="Изображение",
            ),
        ),
    ]
