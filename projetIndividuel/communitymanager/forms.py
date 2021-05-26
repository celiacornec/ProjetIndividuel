from django import forms
from django.shortcuts import render
from .models import Post


class CommentForm(forms.Form):
    commentaire = forms.CharField(required=False, label='Ajouter un commentaire')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur','date_creation',)

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        evenementiel = cleaned_data['evenementiel']
        date_evenement = cleaned_data['date_evenement']

        if (evenementiel and date_evenement == None):
            raise forms.ValidationError('Vous devez choisir une date pour votre évènement.')
        elif (not evenementiel and date_evenement != None):
            raise forms.ValidationError('Vous n\'avez pas coché la case "Evènement.')
        return cleaned_data