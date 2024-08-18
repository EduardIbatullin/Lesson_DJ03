from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_lw_DJ02.urls')),
    path('news/', include('app_lw_DJ03.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)