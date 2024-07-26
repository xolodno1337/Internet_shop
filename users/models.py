from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text='Введите Email')
    avatar = models.ImageField(upload_to="users/avatar", verbose_name="Аватар", help_text="Загрузите аватар",
                               null=True, blank=True, )
    phone = models.CharField(max_length=35, verbose_name="Телефон", blank=True, null=True, help_text='Введите номер '
                                                                                                     'телефона')
    country = models.TextField(blank=True, null=True,  verbose_name="Страна", help_text='Укажите страну')
    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email