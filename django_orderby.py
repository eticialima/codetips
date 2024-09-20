# models.py 
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)  # Nome do produto
  price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
  category = models.CharField(max_length=100)  # Categoria do produto
  
products = Product.objects.order_by('price')

products = Product.objects.order_by('-price')