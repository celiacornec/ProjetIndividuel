from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

""""Fichier qui recense les différents modèles utiles à notre site internet :
communaute, priorite, post et commentaire"""

""""Une communauté possède un nom et une liste d'abonnés"""
class Communaute(models.Model):
    nom = models.CharField(max_length=200)
    abonnes = models.ManyToManyField(User)

    class Meta:
        verbose_name = "communaute"
        ordering = ['nom']

    def __str__(self):
        return self.nom

""""Une priorité possède un label. Les labels existants dans la base de données 
(white, yellow, orange, tomato, red) permettent d'afficher des cercles de couleurs
sur le site internet. D'autres labels ne permettront peut-être pas cette fonctionnalité."""
class Priorite(models.Model):
    label = models.CharField(max_length=200)

    class Meta:
        verbose_name = "priorite"
        ordering = ['label']

    def __str__(self):
        return self.label

"""Un post possède un titre, une description, une date de création. Il peut concerner un évènement
qui se déroule à une certaine date. Il est lié à une certaine communauté et à une certaine priorité."""
class Post(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date_creation = models.DateField(default=timezone.now, verbose_name="Date de création")
    communaute = models.ForeignKey(Communaute, on_delete=models.CASCADE)
    priorite = models.ForeignKey(Priorite, on_delete=models.CASCADE, null=True)
    evenementiel = models.BooleanField(default=False)
    date_evenement = models.DateField(null=True, default=None, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "post"
        ordering = ['date_creation']

    def __str__(self):
        return self.titre

""""Un commentaire possède une date de création, un contenu et un auteur. Il est lié 
à un certain post."""
class Commentaire(models.Model):
    date_creation = models.DateField(default=timezone.now)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "commentaire"
        ordering = ['date_creation']

    def __str__(self):
        return self.contenu
