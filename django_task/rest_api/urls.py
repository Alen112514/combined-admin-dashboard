from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api import views as api_views

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'users', api_views.userViewSet)
router.register(r'products', api_views.productViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include all API routes
    path('api-auth/', include('rest_framework.urls')),  # For login, logout of API
    path('login/', include('login.urls')),  # You can route your login app if needed
    
]
