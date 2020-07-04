from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PodcastIndex.as_view(), name='index'),
    path('podcast/<int:pk>', views.PodcastFilosocast.as_view(), name='podcast'),
    path('sobre/', TemplateView.as_view(template_name="podcasts/sobre.html"), name='sobre'),
    path('contato/', TemplateView.as_view(template_name="podcasts/contato.html"), name='contato'),
    path('podcasters/', TemplateView.as_view(template_name="podcasts/podcasters.html"),
         name='podcasters'),
    path('episodios/', views.PodcastEpisodios.as_view(), name='episodios'),
]
