from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descrição = models.CharField(max_length=450)
    link = models.CharField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to='Portfolio/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo