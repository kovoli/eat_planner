from django.shortcuts import render
from .models import Recept, Category

def rezept_list(request):
    alle_rezepte = Recept.objects.all()

    return render(request, 'rezepte/sites/rezept_list.html', context={'rezepte': alle_rezepte})