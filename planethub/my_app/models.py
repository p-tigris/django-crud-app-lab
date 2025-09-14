from django.db import models
from django.urls import reverse

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=50)
    system = models.CharField(max_length=50)
    planet_type = models.CharField(max_length=50)
    inhabited = models.BooleanField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("planet-detail", kwargs={"planet_id": self.id})
    
    