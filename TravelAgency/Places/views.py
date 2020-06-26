from django.shortcuts import render
from .models import Places

# Create your views here.

def places(request):
    first = Places.objects.exclude(id=4).exclude(id=5).exclude(id=6).exclude(id=7).exclude(id=8).exclude(id=9)
    second =Places.objects.exclude(id=1).exclude(id=2).exclude(id=3).exclude(id=7).exclude(id=8).exclude(id=9)
    third = Places.objects.exclude(id=1).exclude(id=2).exclude(id=3).exclude(id=4).exclude(id=5).exclude(id=6)
    content={'places01': first,'places02': second,'places03': third}
    return render(request,"Places/popular_places.html",content)