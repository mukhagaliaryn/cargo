from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),

    path('', include('main.urls')),
    prefix_default_language=False
)


urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})]