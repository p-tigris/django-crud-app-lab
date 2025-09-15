from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('planets/', views.planets_index, name='planets-index'),
    path('planets/<int:planet_id>', views.planet_detail, name='planet-detail'),
    path('planets/create/', views.PlanetCreate.as_view(), name='planet-create'),
    path('planets/<int:pk>/update/', views.PlanetUpdate.as_view(), name='planet-update'),
    path('planets/<int:pk>/delete/', views.PlanetDelete.as_view(), name='planet-delete'),
    path('planets/<int:planet_id>/add-mission/', views.add_mission, name='add-mission'),
    path('planets/<int:planet_id>/missions/<int:mission_id>/update/', views.update_mission, name='update-mission'),
    path('planets/<int:planet_id>/missions/<int:mission_id>/delete/', views.delete_mission, name='delete-mission'),
    path('accounts/signup/', views.signup, name='signup')
]


