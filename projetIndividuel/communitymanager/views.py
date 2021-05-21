from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CommentForm, PostForm
from .models import Communaute, Post, Commentaire


# Create your views here.

@login_required() #Pensez à mettre ça partout !
def communautes(request, communaute_id=0, choix=2):
    communautes = Communaute.objects.all()
    user = request.user

    if choix == 0:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.remove(request.user)
        #communaute_modif.abonnement = False
    elif choix == 1:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.add(request.user)
        #communaute_modif.abonnement = True

    for communaute in communautes:
        if user in communaute.abonnes.all():
            communaute.abonnement = True
        else:
            communaute.abonnement = False

    return render(request, 'communitymanager/communautes.html', locals())

@login_required()
def communaute(request, communaute_id):
    communaute = Communaute.objects.get(id=communaute_id)
    posts = Post.objects.filter(communaute=communaute)
    return render(request, 'communitymanager/communaute.html', locals())

@login_required()
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    communaute = post.communaute

    form = CommentForm(request.POST or None)
    if form.is_valid():
        contenu_com = form.cleaned_data['commentaire']
        commentaire = Commentaire.objects.create(contenu=contenu_com, post=post, auteur=request.user)

    commentaires = Commentaire.objects.filter(post=post)

    return render(request, 'communitymanager/post.html', locals())

@login_required()
def nouveau_post(request):
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.auteur = request.user
            post.save()
            post_id = post.id
            return redirect('Visualisation post', post_id)
        else:
            return render(request, 'communitymanager/nouveaupost.html', locals())

@login_required()
def modif_post(request):
    form = PostForm

@login_required()
def allposts(request):
    posts = Post.objects.all()
    return render(request, 'communitymanager/posts.html', locals())