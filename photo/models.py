import django
from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import date


class UserName(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя человека на фото')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Имя человека на фото'
        verbose_name_plural = 'Имина людей на фото'


class Photo(models.Model):
    user = models.ForeignKey(User, auto_created=True, on_delete=models.CASCADE, verbose_name="Пользователь")
    photo = models.ImageField(upload_to='file', verbose_name="Фото")
    geo_location = models.CharField(max_length=255, blank=True, verbose_name='Геолокация')
    description = models.TextField(blank=True, verbose_name='Описание')
    names_of_people = models.ManyToManyField(UserName, blank=True, null=True, verbose_name='Люди на фото')
    date_load = models.DateField(auto_created=True, default=date.today, verbose_name='Дата загрузки')

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Фото'
