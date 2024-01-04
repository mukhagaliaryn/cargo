from modeltranslation.translator import translator, TranslationOptions
from .models import Business


class BusinessTranslationOptions(TranslationOptions):
    fields = ('title', 'about', 'description', )


translator.register(Business, BusinessTranslationOptions)
