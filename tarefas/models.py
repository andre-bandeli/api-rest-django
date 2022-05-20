
from django.db import models



class Tarefa(models.Model):
    nome = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


