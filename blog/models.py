from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # define que o modelo é um objeto models.Model indica que o Post é um modelo django, indicando
    # #que deve ser salvo no banco de dados
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#link para outro modelo
    title = models.CharField(max_length=200) #define texto com limite de chars
    text = models.TextField()#Campo nem limite de texto
    created_date = models.DateTimeField(default=timezone.now)#data e hora
    published_date = models.DateTimeField(blank=True, null=True)#data e hora

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #dunder
        return self.title