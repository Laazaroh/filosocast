from django.contrib import admin
from .models import Autor


class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_autor')
    list_display_links = ('id', 'nome_autor')


admin.site.register(Autor, AutorAdmin)
