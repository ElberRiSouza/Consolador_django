from django.db import models
from tinymce import models as tinymce_models

class Postagen(models.Model):
    titulo = models.CharField(max_length=200)
    texto = tinymce_models.HTMLField()
    imagem = models.ImageField(blank=True)
    
    def __str__(self):
        return self.titulo