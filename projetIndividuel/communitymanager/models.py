from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Communaute(models.Model):
    nom = models.CharField(max_length=200)
    abonnes = models.ManyToManyField(User)

    class Meta:
        verbose_name = "communaute"
        ordering = ['nom']

    def __str__(self):
        return self.nom

class Priorite(models.Model):
    label = models.CharField(max_length=200)

    class Meta:
        verbose_name = "priorite"
        ordering = ['label']

    def __str__(self):
        return self.label

class Post(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date_creation = models.DateField(default=timezone.now, verbose_name="Date de parution")
    communaute = models.ForeignKey(Communaute, on_delete=models.CASCADE)
    priorite = models.ForeignKey(Priorite, on_delete=models.CASCADE, null=True)
    evenementiel = models.BooleanField(default=False)
    date_evenement = models.DateField(null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "post"
        ordering = ['date_creation']

    def __str__(self):
        return self.titre