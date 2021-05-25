from django import forms
from django.shortcuts import render
from .models import Post


class CommentForm(forms.Form):
    commentaire = forms.CharField(required=False, label='Ajouter un commentaire')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur','date_creation',)

