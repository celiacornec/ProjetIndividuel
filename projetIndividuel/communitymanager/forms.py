from django import forms
from django.shortcuts import render
from .models import Post


class CommentForm(forms.Form):
    commentaire = forms.CharField(required=False, label='Commentaire')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['assignee'].queryset = self.instance.project.members