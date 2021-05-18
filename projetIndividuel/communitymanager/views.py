from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Communaute

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

    return render(request, 'communautes.html', locals())

@login_required()
def abonnement(request, communaute, choix):
    communaute = Communaute.objects.all(nom=communaute)
    if choix == 1:
        communaute.abonnes.remove(request.user)
    else:
        communaute.abonnes.add(request.user)

    return render(request, 'communautes.html', locals())
