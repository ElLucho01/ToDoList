from django.db import models

# Create your models here.

class Lista(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    complete = models.BooleanField()
    def __str__(self):
        return self.text