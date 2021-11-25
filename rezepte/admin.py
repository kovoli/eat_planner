from django.contrib import admin
from .models import Recept, Category


@admin.register(Recept)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #list_filter = ('status', 'created', 'publish', 'author')
    #search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('name',)}
    #raw_id_fields = ('author',)


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    #list_filter = ('status', 'created', 'publish', 'author')
    #search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('name',)}
    #raw_id_fields = ('author',)