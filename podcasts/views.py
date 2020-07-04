from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Podcast
from autores.models import Autor


class PodcastIndex(ListView):
    model = Podcast
    template_name = 'podcasts/index.html'
    context_object_name = 'podcasts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')

        return qs


class PodcastFilosocast(DetailView):
    model = Podcast
    template_name = 'podcasts/episodio.html'
    context_object_name = 'podcast'


class PodcastEpisodios(ListView):
    model = Podcast
    template_name = 'podcasts/episodios.html'
    context_object_name = 'podcasts'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['autores'] = Autor.objects.all()
        return context
