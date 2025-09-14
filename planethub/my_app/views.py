from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Planet, Mission

from .forms import MissionForm, MissionDeleteForm
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

    mission_form = MissionForm()
    return render(request, 'planets/detail.html', { 'planet': planet, 'mission_form': mission_form })

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

def add_mission(request, planet_id):
    form = MissionForm(request.POST)

    if form.is_valid():
        new_mission = form.save(commit=False)
        new_mission.planet_id = planet_id
        new_mission.save()
    return redirect('planet-detail', planet_id=planet_id)

def update_mission(request, planet_id, mission_id):
    mission = Mission.objects.get(id=mission_id)
    form = MissionForm(request.POST, instance=mission)
    template_name = 'my_app/mission_update_form.html'

    if form.is_valid():
        form.save()
        return redirect('planet-detail', planet_id=planet_id)

    return render(request, template_name, { 'mission': mission, 'mission_form': form,'planet_id': planet_id, 'mission_id': mission_id })

def delete_mission(request, planet_id, mission_id):
    mission = Mission.objects.get(id=mission_id)

    mission.delete()
    return redirect('planet-detail', planet_id=planet_id)