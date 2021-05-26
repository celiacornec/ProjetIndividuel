from django import forms
from .models import Post
from django.forms import widgets

"""Ce fichier contient tous les formulaires utiles dans le site internet :
formulaires d'ajout d'un post et d'ajout d'un commentaire."""


"""Formulaire permettant à un utilisateur d'entrer un commentaire"""
class CommentForm(forms.Form):
    commentaire = forms.CharField(required=False, label='Ajouter un commentaire')

"""Formulaire permettant à un utilisateur de créer un post et de le modifier."""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur','date_creation',)
        widgets = {
            'date_evenement': widgets.SelectDateWidget(empty_label=("Année", "Mois", "Jour")),
        }

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        # Permet notamment d'assurer la saisie d'une date valide
        if 'date_evenement' in cleaned_data.keys():
            evenementiel = cleaned_data['evenementiel']
            date_evenement = cleaned_data['date_evenement']

            # Permet de lier le fait de déclarer un évènement et le fait de lui donner une date
            if (evenementiel and date_evenement == None):
                raise forms.ValidationError('Vous devez choisir une date pour votre évènement.')
            elif (not evenementiel and date_evenement != None):
                raise forms.ValidationError('Vous n\'avez pas coché la case "Evènement.')
            return cleaned_data