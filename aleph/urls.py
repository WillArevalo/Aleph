"""aleph URL Configuration"""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
	# Admin
    path('admin/', admin.site.urls),
    # Accounts
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', TemplateView.as_view(template_name="home.html")),
    path('abilities/',include(('abilities.urls','abilities'),namespace='abilities')),
    path('vacancies/', include(('vacancies.urls', 'vacancies'),namespace='vacancies')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
