from django.urls import path
from .views import rezepte_list


app_name = 'rezepte'

urlpatterns = [
    path('', rezepte_list, name='rezepte_liste'),
]
