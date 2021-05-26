from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import CommentForm, PostForm
from .models import Communaute, Post, Commentaire

"""Ce fichier permet de créer des vues qui utilisent les modèles, formulaires
et templates pour permettre l'affichage des pages du site internet et les interactions
avec l'utilisateur"""

"""Permet d'afficher la liste des communautés et de donner la possibilité à 
l'utilisateur de s'abonner ou de se désabonner de ces communautés"""
@login_required()  # Permet de ne donner accès à la vue qu'aux utilisateurs identifiés
def communautes(request, communaute_id=0, choix=2):
    communautes = Communaute.objects.all()
    user = request.user

    for communaute in communautes:
        communaute.nb_posts = Post.objects.filter(communaute=communaute).count()

    #Retire un utilisateur de la liste des abonnés d'une communauté lors du désabonnement
    if choix == 0:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.remove(request.user)
    #Ajoute un utilisateur à la liste des abonnés d'une communauté lors de l'abonnement
    elif choix == 1:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.add(request.user)

    for communaute in communautes:
        if user in communaute.abonnes.all():
            communaute.abonnement = True
        else:
            communaute.abonnement = False

    return render(request, 'communitymanager/communautes.html', locals())

"""Permet d'afficher les posts d'une certaine communaute, par ordre
antechronologique"""
@login_required()
def communaute(request, communaute_id):
    communaute = Communaute.objects.get(id=communaute_id)
    posts = Post.objects.filter(communaute=communaute).order_by('-date_creation')
    return render(request, 'communitymanager/communaute.html', locals())

"""Permet à un utilisateur de visualiser un post et ses caractéristiques,
ainsi que d'ajouter un commentaire"""
@login_required()
def post(request, post_id, droitmodif=1):
    post = Post.objects.get(id=post_id)
    communaute = post.communaute

    #Formulaire permettant l'ajout d'un commentaire
    form = CommentForm(request.POST or None)
    if form.is_valid():
        contenu_com = form.cleaned_data['commentaire']
        commentaire = Commentaire.objects.create(contenu=contenu_com, post=post, auteur=request.user)

    commentaires = Commentaire.objects.filter(post=post)

    return render(request, 'communitymanager/post.html', locals())

""""Permet à un utilisateur de créer un nouveau post"""
@login_required()
def nouveau_post(request):
    form = PostForm(request.POST or None)
    #Sauvegarde les données du post si le formulaire est valide
    if form.is_valid():
        post = form.save(commit=False)
        post.auteur = request.user
        post.date_creation = timezone.now()
        post.save()
        post_id = post.id
        return redirect('Visualisation post', post_id)
    else:
        return render(request, 'communitymanager/nouveaupost.html', locals())


""""Permet à un utilisateur de modifier un post s'il en est l'auteur"""
@login_required()
def modif_post(request, post_id):
    post = Post.objects.get(id=post_id)

    #Vérifie si l'utilisateur est bien l'auteur du post
    if request.user == post.auteur:
        droitmodif = 1
        if request.method == 'POST':
            #Préremplissage du formulaire avec les données actuelles du post
            form = PostForm(request.POST or None, instance=post)
            if form.is_valid():
                form.save()
                return redirect('Visualisation post', post_id)
            else:
                return render(request, 'communitymanager/modifpost.html', locals())
        else:
            form = PostForm(instance=post)
            return render(request, 'communitymanager/modifpost.html', locals())

    #Envoi un message d'erreur si l'utilisateur souhaite modifier et n'est pas l'auteur du post
    else:
        droitmodif = 0
        return redirect('Refus modif post', post_id, droitmodif)


""""Permet l'affichage des posts correspondant aux communautés auxquelles 
l'utilisateur est abonné"""
@login_required()
def allposts(request):
    communautes = Communaute.objects.filter(abonnes=request.user)
    posts = Post.objects.filter(communaute__in=communautes).order_by('-date_creation')
    return render(request, 'communitymanager/posts.html', locals())
