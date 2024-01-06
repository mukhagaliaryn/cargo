from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('about/corp/', views.about_corp, name='corp'),
    path('about/org/', views.about_org, name='org'),
    path('business/<pk>/', views.business_detail, name='business'),
    path('logistic/<pk>/', views.logistic_detail, name='logistic'),
]
