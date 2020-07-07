from django.db import models
from django.utils import timezone
from autores.models import Autor


class Podcast(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now())
    descricao = models.TextField()
    excerto = models.TextField(max_length=250, default=None)
    imagem = models.ImageField(
        upload_to='podcast_img/%Y/%m/%d')
    audio = models.FileField(upload_to='podcast_audio/%Y/%m/%d')

    def __str__(self):
        return self.titulo
