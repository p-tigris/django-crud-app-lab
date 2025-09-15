from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Planet, Mission

from .forms import MissionForm
# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def planets_index(request):
    planets = Planet.objects.filter(user=request.user)
    return render(request, 'planets/index.html', { 'planets': planets })

@login_required
def planet_detail(request, planet_id):
    planet = Planet.objects.get(id=planet_id)

    mission_form = MissionForm()
    return render(request, 'planets/detail.html', { 'planet': planet, 'mission_form': mission_form })

class PlanetCreate(LoginRequiredMixin, CreateView):
    model = Planet
    fields = ['name', 'system', 'planet_type', 'inhabited', 'description']
    template_name = 'my_app/planet_form.html'

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)
    
class PlanetUpdate(LoginRequiredMixin, UpdateView):
    model = Planet
    fields = ['system', 'planet_type', 'inhabited', 'description']

class PlanetDelete(LoginRequiredMixin, DeleteView):
    model = Planet
    success_url = '/planets/'

@login_required
def add_mission(request, planet_id):
    form = MissionForm(request.POST)

    if form.is_valid():
        new_mission = form.save(commit=False)
        new_mission.planet_id = planet_id
        new_mission.save()
    return redirect('planet-detail', planet_id=planet_id)

@login_required
def update_mission(request, planet_id, mission_id):
    mission = Mission.objects.get(id=mission_id)
    form = MissionForm(request.POST, instance=mission)
    template_name = 'my_app/mission_update_form.html'

    if form.is_valid():
        form.save()
        return redirect('planet-detail', planet_id=planet_id)

    return render(request, template_name, { 'mission': mission, 'mission_form': form,'planet_id': planet_id, 'mission_id': mission_id })

@login_required
def delete_mission(request, planet_id, mission_id):
    mission = Mission.objects.get(id=mission_id)

    mission.delete()
    return redirect('planet-detail', planet_id=planet_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('planets-index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    return render(request, 'signup.html', { 'form': form, 'error_message': error_message })