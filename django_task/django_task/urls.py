from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('api/', include('rest_api.urls')),
    # Catch-all pattern for React frontend
    path('', TemplateView.as_view(template_name="index.html")),
]
