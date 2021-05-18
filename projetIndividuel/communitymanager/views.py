from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Communaute, Post


# Create your views here.

@login_required() #Pensez à mettre ça partout !
def communautes(request):
    communautes = Communaute.objects.all()
    user = request.user
    for communaute in communautes:
        if user in communaute.abonnes.all():
            communaute.abonnement = True
        else:
            communaute.abonnement = False
    return render(request, 'communitymanager/communautes.html', locals())

@login_required()
def modifabonnement(request, communaute_id, choix):
    communaute = Communaute.objects.get(id=communaute_id)
    if choix == 0:
        communaute.abonnes.remove(request.user)
    else:
        communaute.abonnes.add(request.user)
    return render(request, 'communitymanager/communautes.html', locals())

@login_required()
def communaute(request, communaute_id):
    communaute = Communaute.objects.get(id=communaute_id)
    posts = Post.objects.all(communaute=communaute)
    return render(request, 'communitymanager/communaute.html', locals())
