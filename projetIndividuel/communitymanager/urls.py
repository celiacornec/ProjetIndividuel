from django.urls import path
from .import views

urlpatterns = [
    path('communautes', views.communautes, name='Liste des communautés'),
    path('abonnement/<int:communaute_id>/<int:choix>', views.modifabonnement, name='Modification abonnement'),
    path('communaute/<int:communaute_id>', views.communaute, name='Affichage des posts'),
]