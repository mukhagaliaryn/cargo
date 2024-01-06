from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Offer, Business, Logistic, News


class OfferAdmin(TranslationAdmin):
    pass


class BusinessAdmin(TranslationAdmin):
    pass


class LogisticAdmin(TranslationAdmin):
    pass


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Logistic, LogisticAdmin)
admin.site.register(News)
