from django import forms
from .models import Pret, Materiel, Enseignant

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Pret
        fields = ['emprunte_par', 'salle']

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = '__all__'

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'
