from django.db import models
from ckeditor.fields import RichTextField


class Offer(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    about = models.TextField(verbose_name='О деятельности', blank=True, null=True)
    poster = models.ImageField(verbose_name='Обложка', upload_to='main/business/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'


class Business(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    about = models.CharField(verbose_name='О деятельности', max_length=255)
    poster = models.ImageField(verbose_name='Обложка', upload_to='main/business/')
    description = RichTextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельности'


class Logistic(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    about = models.TextField(verbose_name='О деятельности', blank=True, null=True)
    poster = models.ImageField(verbose_name='Обложка', upload_to='main/business/')
    description = RichTextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Логистика'
        verbose_name_plural = 'Логистики'


class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = RichTextField(verbose_name='Описание', blank=True, null=True)
    poster = models.ImageField(verbose_name='Обложка', upload_to='main/news/')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

