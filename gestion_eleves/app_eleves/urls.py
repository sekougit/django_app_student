from django.urls import path
from .views import liste_eleves, detail_eleve, ajouter_modifier_eleve, supprimer_eleve, modifier_eleve

app_name = 'app_eleves' 

from django.urls import path
from . import views

app_name = 'app_eleves'

urlpatterns = [
    path('liste_eleves/', views.ajouter_modifier_eleve, name='liste_eleves'),
    path('ajouter/', ajouter_modifier_eleve, name='ajouter_eleve'),
    path('eleve/<int:id>/', detail_eleve, name='detail_eleve'),
    path('modifier/<int:id>/', modifier_eleve, name='modifier_eleve'),
    path('supprimer/<int:id>/', supprimer_eleve, name='supprimer_eleve'),
]
