from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Pokemon, Evolution


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

class PokemonDetail(DetailView):
    model = Pokemon
    template_name = "pokemon_detail.html"

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'img', 'bio', 'verified_pokemon']
    template_name = "pokemon_update.html"
    success_url = "/pokedex/"

class PokemonDelete(DeleteView):
    model = Pokemon
    template_name = "pokemon_delete_confirmation.html"
    success_url = "/pokedex/"

class EvolutionCreate(View):
    def post(self, request, pk):
        name = request.POST.get("name")
        Evolution.objects.create(name=name)
        return redirect('pokemon_detail', pk=pk)