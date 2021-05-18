from django.urls import path
from . import views

urlpatterns = [
    path('communautes', views.communautes, name='Liste des communautés'),
    path('abonnement/<')
]