from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name} ({self.id})" 
    
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    volume = models.CharField(max_length=10)
    description = models.CharField(max_length=225)
    image = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name} ({self.id})"
# Create your models here.
