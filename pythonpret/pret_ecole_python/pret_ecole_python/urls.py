# Assurez-vous que l'instruction 'include' ne fait pas référence à 'pret_ecole_python_mange.urls' de manière récursive.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prets/', include('pret_ecole_python_mange.urls')), # Assurez-vous qu'aucun fichier 'urls.py' ne s'auto-inclut
    # Autres patterns d'URL de votre projet
]