# models.py 
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)  # Nome do produto
  price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
  category = models.CharField(max_length=100)  # Categoria do produto


from django.db.models import Sum, Avg, Count, Max

# Calcula a soma total de todos os preços dos produtos
total_price = Product.objects.aggregate(Sum('price')).get('price__sum')

# Calcula o preço médio de todos os produtos
average_price = Product.objects.aggregate(Avg('price')).get('price__avg')

# Conta o número total de produtos
product_count = Product.objects.aggregate(Count('id')).get('price__count')  # Deveria usar 'id__count', pois 'price__count' está incorreto

# Obtém o valor do produto mais caro
most_expensive_product = Product.objects.aggregate(Max('price')).get('price__max')
