from django.urls import path
from .views import (
    home, 
    ListeMaterielsView, 
    DetailMaterielView, 
    EmpruntMaterielView,
    CreerMaterielView,
    CreerEnseignantView
)

app_name = 'pret_ecole_python_mange'

urlpatterns = [
    path('', home, name='home'),
    path('materiels/', ListeMaterielsView.as_view(), name='liste_materiels'),
    path('materiels/<int:pk>/', DetailMaterielView.as_view(), name='detail_materiel'),
    path('materiels/<int:pk>/emprunter/', EmpruntMaterielView.as_view(), name='emprunt_materiel'),
    path('creer_materiel/', CreerMaterielView.as_view(), name='creer_materiel'),
    path('creer_enseignant/', CreerEnseignantView.as_view(), name='creer_enseignant'),
    # Plus de routes peuvent être ajoutées ici
]
