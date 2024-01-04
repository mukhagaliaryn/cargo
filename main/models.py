from django.db import models
from django.utils.translation import gettext_lazy as _


class Business(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255)
    about = models.CharField(verbose_name=_('О деятельности'), max_length=255)
    poster = models.ImageField(verbose_name=_('Обложка'), upload_to='main/business/')
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Деятельность')
        verbose_name_plural = _('Деятельности')


class Logistic(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255)
    about = models.CharField(verbose_name=_('О деятельности'), max_length=255)
    poster = models.ImageField(verbose_name=_('Обложка'), upload_to='main/business/')
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Логистика')
        verbose_name_plural = _('Логистики')


class News(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255)
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)
    poster = models.ImageField(verbose_name=_('Обложка'), upload_to='main/news/')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

