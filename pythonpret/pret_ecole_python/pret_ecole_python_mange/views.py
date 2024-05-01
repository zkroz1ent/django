from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Enseignant, Salle, Materiel, Accessoire, Budget, Pret
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import EmpruntForm, MaterielForm, EnseignantForm

def home(request):
    return render(request, 'home.html')

class ListeMaterielsView(ListView):
    model = Materiel
    template_name = 'liste_materiels.html'
    context_object_name = 'materiels'

class DetailMaterielView(DetailView):
    model = Materiel
    template_name = 'detail_materiel.html'
    context_object_name = 'materiel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prets'] = Pret.objects.filter(materiel=self.object)
        return context

class EmpruntMaterielView(View):
    def post(self, request, pk):
        materiel = get_object_or_404(Materiel, pk=pk)
        form = EmpruntForm(request.POST)
        if form.is_valid():
            Pret.objects.create(
                materiel=materiel,
                emprunte_par=form.cleaned_data['emprunte_par'],
                salle=form.cleaned_data['salle']
            )
            return redirect(reverse('pret_ecole_python_mange:detail_materiel', kwargs={'pk': materiel.pk}))
        return HttpResponse("Invalid form", status=400)

class CreerMaterielView(View):
    def get(self, request):
        form = MaterielForm()
        return render(request, 'creer_materiel.html', {'form': form})

    def post(self, request):
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pret_ecole_python_mange:liste_materiels'))
        return HttpResponse("Invalid form", status=400)

class CreerEnseignantView(View):
    def get(self, request):
        form = EnseignantForm()
        return render(request, 'creer_enseignant.html', {'form': form})

    def post(self, request):
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pret_ecole_python_mange:home'))
        return HttpResponse("Invalid form", status=400)

# Plus d'implémentations de vues ici...
