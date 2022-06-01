from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Pokemon

class Home(TemplateView):
    template_name = "home.html"


class PokemonList(TemplateView):
    template_name = "pokemon_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pokemon"] = Pokemon.objects.all()
        return context