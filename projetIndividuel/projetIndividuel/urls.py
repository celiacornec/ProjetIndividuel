from django.contrib import admin
from django.urls import path, include

""""Ce fichier recense tous les chemins, ou urls, permettant d'accéder aux vues créées, 
pour le projet global."""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('communitymanager/', include('communitymanager.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
