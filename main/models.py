from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Lista(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listasDB", null=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    complete = models.BooleanField()
    def __str__(self):
        return self.text