from django.shortcuts import render


def rezepte_list(request):
    return render(request, 'rezepte/base.html',)