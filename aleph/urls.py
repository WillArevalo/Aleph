"""aleph URL Configuration"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TemplateView.as_view(template_name="test.html")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
