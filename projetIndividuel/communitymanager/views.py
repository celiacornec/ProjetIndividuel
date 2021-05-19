from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Communaute, Post


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
def modifabonnement(request, communaute_id, choix):
    communaute = Communaute.objects.get(id=communaute_id)
    if choix == 0:
        communaute.abonnes.remove(request.user)
        communaute.abonnement = False
    else:
        communaute.abonnes.add(request.user)
        communaute.abonnement = True
    communautes = Communaute.objects.all()
    return render(request, 'communitymanager/communautes.html', locals())

@login_required()
def communaute(request, communaute_id):
    communaute = Communaute.objects.get(id=communaute_id)
    posts = Post.objects.filter(communaute=communaute)
    return render(request, 'communitymanager/communaute.html', locals())
