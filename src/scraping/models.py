from django.db import models
from .utils import from_cyrillic_to_eng


# Create your models here.


class City(models.Model):
    name_city = models.CharField(max_length=50,verbose_name='Название населенного пункта',
                                 unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'

    def __str__(self):
        return self.name_city

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name_city))
        super().save(*args, **kwargs)


class Programming_language(models.Model):
    name_city = models.CharField(max_length=50,
                                 verbose_name='Язык програмирования', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык програмирования'
        verbose_name_plural = 'Языки програмирования'

    def __str__(self):
        return self.name_city

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name_city))
        super().save(*args, **kwargs)

class Vacancy(models.Model):
    urls = models.URLField(unique=True)
    title = models.CharField(max_length=250,
                             verbose_name='Заголовок компании')
    company = models.CharField(max_length=250,
                               verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name= 'Город')
    language = models.ForeignKey('Programming_language',
                                 on_delete=models.CASCADE,verbose_name='Язык програмирования')

    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

