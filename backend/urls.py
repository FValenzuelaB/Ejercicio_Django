from django.contrib import admin
from django.urls import path, include

#añadir para manejo de imagenes
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
]

#añadir para manejo de imagenes
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)