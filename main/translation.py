from modeltranslation.translator import translator, TranslationOptions
from .models import Business, Offer, Logistic


class OfferTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


class BusinessTranslationOptions(TranslationOptions):
    fields = ('title', 'about', 'description', )


class LogisticTranslationOptions(TranslationOptions):
    fields = ('title', 'about', 'description', )


translator.register(Business, BusinessTranslationOptions)
translator.register(Logistic, LogisticTranslationOptions)
translator.register(Offer, OfferTranslationOptions)
