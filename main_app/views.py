from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"



class Pokemon:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


pokedex = [
  Pokemon("Charmander",
          "https://www.nicepng.com/png/detail/278-2789894_pokemon-charmander-vector.png",
          "A cute fire pokemon."),
  Pokemon("Pikachu",
          "https://www.nicepng.com/png/detail/485-4856027_pikachu-pikachu-ears-cute-pikachu-cute-pokemon-pokemon.png",
          "A yellow rat."),
  Pokemon("Lugia",
          "https://www.nicepng.com/png/detail/225-2258279_pokmon-lugia-or-latios-lugia-pokemon.png",
          "A white bird."),
  Pokemon("Mew",
          "https://www.nicepng.com/png/detail/62-622852_ignore-words-mew-png.png",
          "An alien."),
  Pokemon("Magikarp",
          "https://www.nicepng.com/png/detail/149-1492459_magikarp-pokemon-go-magikarp.png",
          "Sushi."),
  Pokemon("Hitmonlee",
          "https://www.kindpng.com/picc/m/276-2765609_pokemon-hitmonlee-png-transparent-png.png",
          "Bruce Lee as a Pokemon."),
]
class PokemonList(TemplateView):
    template_name = "pokemon_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pokedex"] = pokedex
        return context