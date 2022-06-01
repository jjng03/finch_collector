from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Pokemon

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
    success_url = "/pokedex/"