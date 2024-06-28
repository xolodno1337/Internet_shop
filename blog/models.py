from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок")
    slug = models.CharField(max_length=100, verbose_name='Slug', **NULLABLE)
    body = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое блога")
    image = models.ImageField(upload_to="picture_blog/", verbose_name="Изображение",
                              help_text="Загрузите фото продукта", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.title}: {self.is_active}'

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "is_active", "created_at", "body"]
