from django.urls import path
from .views import rezept_list


app_name = 'rezepte'

urlpatterns = [
    path('rezepte/', rezept_list, name='rezept_liste'),
]
