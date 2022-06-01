from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('pokedex/', views.PokemonList.as_view(), name="pokemon_list"),
    path('pokedex/new/', views.PokemonCreate.as_view(), name="pokemon_create"),
    path('pokedex/<int:pk>/', views.PokemonDetail.as_view(), name="pokemon_detail"),
    path('pokedex/<int:pk>/update', views.PokemonUpdate.as_view(), name="pokemon_update"),
    path('pokedex/<int:pk>/delete', views.PokemonDelete.as_view(), name="pokemon_delete"),
    path('pokedex/<int:pk>/evolutions/new/', views.EvolutionCreate.as_view(), name="evolution_create")
]