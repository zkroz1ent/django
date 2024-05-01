from django.db import models
from django.contrib.auth.models import User

class Enseignant(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Salle(models.Model):
    code = models.CharField(max_length=10, unique=True, default='Inconnu')
    etage = models.IntegerField()

    def __str__(self):
        return f"Salle {self.code}"

class Budget(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    achete_par = models.CharField(max_length=100, default='Inconnu')
    proprietaire = models.ForeignKey(Enseignant, related_name='materiels', on_delete=models.SET_NULL, null=True)
    salle_stockage = models.ForeignKey(Salle, related_name='materiels', on_delete=models.SET_NULL, null=True)
    budget = models.ForeignKey(Budget, related_name='materiels', on_delete=models.SET_NULL, null=True)
    etat = models.CharField(max_length=100, default='Bon')

    def __str__(self):
        return f"Materiel: {self.nom}"

class Accessoire(models.Model):
    materiel = models.ForeignKey(Materiel, related_name='accessoires', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"Accessoire: {self.nom} pour {self.materiel.nom}"

class Pret(models.Model):
    materiel = models.ForeignKey(Materiel, related_name='prets', on_delete=models.CASCADE)
    emprunte_par = models.ForeignKey(Enseignant, related_name='prets', on_delete=models.SET_NULL, null=True)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour = models.DateTimeField(null=True, blank=True)
    salle = models.ForeignKey(Salle, related_name='prets', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Pret de {self.materiel.nom} à {self.emprunte_par}"

