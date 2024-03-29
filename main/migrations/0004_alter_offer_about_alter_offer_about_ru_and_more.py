# Generated by Django 5.0.1 on 2024-01-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='about',
            field=models.TextField(max_length=255, verbose_name='О деятельности'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='about_ru',
            field=models.TextField(max_length=255, null=True, verbose_name='О деятельности'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='about_zh_hans',
            field=models.TextField(max_length=255, null=True, verbose_name='О деятельности'),
        ),
    ]
