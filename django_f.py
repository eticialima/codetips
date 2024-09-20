# models.py 
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)  # Nome do produto
  price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
  category = models.CharField(max_length=100)  # Categoria do produto
 
  
# views.py
from django.db.models import F, Avg

average_price = Product.objects.aggregate(average_price=Avg('price')).get('average_price')

products = Product.objects.filter(price__gt=F('price') * 2)