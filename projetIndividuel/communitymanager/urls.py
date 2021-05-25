from django.urls import path
from .import views

urlpatterns = [
    path('communautes', views.communautes, name='Liste des communautes'),
    path('communautes/<int:communaute_id>/<int:choix>', views.communautes, name='Modification abonnement'),
    path('communaute/<int:communaute_id>', views.communaute, name='Liste des posts'),
    path('post/<int:post_id>', views.post, name='Visualisation post'),
    path('nouveaupost/', views.nouveau_post, name="Nouveau post"),
    path('modifpost/<int:post_id>', views.modif_post, name="Modification post"),
    path('posts', views.allposts, name="Affichage de tous les posts"),
]