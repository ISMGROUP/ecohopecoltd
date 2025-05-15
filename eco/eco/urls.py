from django.contrib import admin
from django.urls import path, include  # Use include for app URLs
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecohope.urls')),  # This will include all ecohope app URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
