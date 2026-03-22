from django.db import models

# Create your models here.

class Tag(models.Model):
    nome = models.CharField(max_length=50)

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=500)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
