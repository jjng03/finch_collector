from django.db import models

class Pokemon(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_pokemon = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Evolution(models.Model):

    name = models.CharField(max_length=150)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="evolutions")

    def __str__(self):
        return self.name