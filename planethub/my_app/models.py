from django.db import models
from django.urls import reverse

MISSIONS = [
    ('study', 'Study & Survey'),
    ('trade', 'Trade'),
    ('defense', 'Defense'),
    ('other', 'Other')
]

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

class Mission(models.Model):
    type = models.CharField(max_length=10, choices=MISSIONS, default=MISSIONS[0][0])
    date = models.DateField("Mission Start Date")

    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
    
    
    