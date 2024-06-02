from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Наименование")
    category_description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование " "продукта",
    )
    product_description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    product_picture = models.ImageField(
        upload_to="picture_product/",
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
    )
    price = models.DecimalField(verbose_name="Цена", help_text="Введите цену")
    date_creation = models.DateField(verbose_name="Дата создания")
    date_change = models.DateTimeField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.product_name}: {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["product_name", "product_category", "price"]
