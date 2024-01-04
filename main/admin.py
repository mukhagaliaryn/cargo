from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Business, Logistic, News


class BusinessAdmin(TranslationAdmin):
    pass


# Register your models here.
admin.site.register(Business, BusinessAdmin)
admin.site.register(Logistic)
admin.site.register(News)
