from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Planet
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def planets_index(request):
    planets = Planet.objects.all()
    return render(request, 'planets/index.html', { 'planets': planets })

def planet_detail(request, planet_id):
    planet = Planet.objects.get(id=planet_id)

    return render(request, 'planets/detail.html', { 'planet': planet })

class PlanetCreate(CreateView):
    model = Planet
    fields = '__all__'
    template_name = 'my_app/planet_form.html'

    def form_valid(self, form):

        return super().form_valid(form)
    
class PlanetUpdate(UpdateView):
    model = Planet
    fields = ['system', 'planet_type', 'inhabited', 'description']

class PlanetDelete(DeleteView):
    model = Planet
    success_url = '/planets/'