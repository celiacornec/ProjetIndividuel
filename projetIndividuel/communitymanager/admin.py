from django.contrib import admin
from .models import Communaute, Priorite, Post, Commentaire

"""Enregistrement des modèles à prendre en compte par l'administration"""
admin.site.register(Communaute)
admin.site.register(Priorite)
admin.site.register(Post)
admin.site.register(Commentaire)
