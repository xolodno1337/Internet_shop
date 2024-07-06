# Generated by Django 5.0.6 on 2024-07-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото продукта",
                null=True,
                upload_to="picture_blog/",
                verbose_name="Изображение",
            ),
        ),
    ]