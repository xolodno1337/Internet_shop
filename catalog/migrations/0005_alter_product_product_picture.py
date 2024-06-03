# Generated by Django 5.0.6 on 2024-06-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_product_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_picture",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото продукта",
                null=True,
                upload_to="picture_product/",
                verbose_name="Изображение",
            ),
        ),
    ]
