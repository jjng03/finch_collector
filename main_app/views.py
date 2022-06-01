from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Pokemon
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html"


class PokemonList(TemplateView):
    template_name = "pokemon_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["pokemon"] = Pokemon.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["pokemon"] = Pokemon.objects.all()
            context["header"] = "All Pokemon"
        return context

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'img', 'bio', 'verified_pokemon']
    template_name = "pokemon_create.html"
    def get_success_url(self):
        return reverse('pokemon_detail', kwargs={'pk: self.object.pk'})

class PokemonDetail(DetailView):
    model = Pokemon
    template_name = "pokemon_detail.html"

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'img', 'bio', 'verified_pokemon']
    template_name = "pokemon_update.html"
    def get_success_url(self):
        return reverse('pokemon_detail', kwargs={'pk': self.object.pk})

class PokemonDelete(DeleteView):
    model = Pokemon
    template_name = "pokemon_delete_confirmation.html"
    success_url = "/pokedex/"