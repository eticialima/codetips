# models.py 
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)  # Nome do produto
  price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
  category = models.CharField(max_length=100)  # Categoria do produto
  
# views.py
from django.db.models import Q

products = Product.objects.filter(
  Q(price__gt=100) | Q(category='Electronics')
)