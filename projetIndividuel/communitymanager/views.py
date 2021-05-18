from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Communaute

# Create your views here.

@login_required() #Pensez à mettre ça partout !
def communautes(request):
    communautes = Communaute.objects.all()
    user = request.user
    return render(request, 'communautes.html', locals())