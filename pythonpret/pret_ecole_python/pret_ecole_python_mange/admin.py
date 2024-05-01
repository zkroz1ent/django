from django.contrib import admin
from .models import Enseignant, Salle, Materiel, Accessoire, Budget, Pret

# Enregistrement des modèles pour les rendre accessibles dans l'interface d'administration
admin.site.register(Enseignant)
admin.site.register(Salle)
admin.site.register(Materiel)
admin.site.register(Accessoire)
admin.site.register(Budget)
admin.site.register(Pret)
