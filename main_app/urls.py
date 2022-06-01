from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('pokedex/', views.PokemonList.as_view(), name="pokemon_list"),
    path('pokedex/new/', views.PokemonCreate.as_view(), name="pokemon_create"),
    path('pokedex/<int:pk>/', views.PokemonDetail.as_view(), name="pokemon_detail")
]