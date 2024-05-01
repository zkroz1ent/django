from django.test import TestCase
from .models import Enseignant, Salle, Materiel

class EnseignantModelTest(TestCase):
    
    def setUp(self):
        Enseignant.objects.create(prenom='John', nom='Doe')

    def test_string_representation(self):
        enseignant = Enseignant.objects.get(id=1)
        self.assertEqual(str(enseignant), 'John Doe')

class SalleModelTest(TestCase):

    def setUp(self):
        Salle.objects.create(code='001', etage=0)

    def test_string_representation(self):
        salle = Salle.objects.get(id=1)
        self.assertEqual(str(salle), 'Salle 001')

class MaterielModelTest(TestCase):

    def setUp(self):
        enseignant = Enseignant.objects.create(prenom='Jane', nom='Doe')
        salle = Salle.objects.create(code='002', etage=1)
        Materiel.objects.create(nom='Projecteur', proprietaire=enseignant, salle_stockage=salle)

    def test_string_representation(self):
        materiel = Materiel.objects.get(id=1)
        self.assertEqual(str(materiel), 'Materiel: Projecteur')
