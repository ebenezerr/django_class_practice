from importlib.resources import path
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include("apps.inventory.urls", namespace="inventory"))
]
