# Generated by Django 5.0.1 on 2024-01-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='about_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='О деятельности'),
        ),
        migrations.AddField(
            model_name='business',
            name='about_zh_hans',
            field=models.CharField(max_length=255, null=True, verbose_name='О деятельности'),
        ),
        migrations.AddField(
            model_name='business',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='business',
            name='description_zh_hans',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='business',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='business',
            name='title_zh_hans',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]
