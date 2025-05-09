from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', include('accounts.urls')),
    path('search/', include('openmedia.urls')),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)