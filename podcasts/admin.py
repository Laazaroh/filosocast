from django.contrib import admin
from .models import Podcast


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'data',)
    list_display_links = ('id', 'titulo',)


admin.site.register(Podcast, PodcastAdmin)
