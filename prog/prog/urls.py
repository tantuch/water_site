from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('waterbiektau/', include('water.urls')),
    path('waterbiektau/admin/', admin.site.urls),
]
