from django.db import models

# Create your models here.

class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    email = models.EmailField(max_length=254)
    
    class Meta:
        ordering = ['created']