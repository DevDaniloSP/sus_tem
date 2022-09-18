from django.db import models

class Medicamento(models.Model):
    nome = models.CharField(max_length=255,blank=False)
    local = models.CharField(max_length=255 ,blank=False , verbose_name= 'Local de dispensação')

    def __str__(self):
        return self.nome

