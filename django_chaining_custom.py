from django.db import models

# Gerenciador personalizado para o modelo Product
class ProductManager(models.Manager):
  
  # Método que retorna produtos com preço maior que 100
  def get_expensive_products(self):
    return self.filter(price__gt=100)
  
  # Método que filtra produtos pela categoria especificada
  def get_filtered_products(self, category):
    return self.filter(category=category)
  
# Modelo Product que representa um produto
class Product(models.Model):
  name = models.CharField(max_length=100)  # Nome do produto
  price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
  category = models.CharField(max_length=100)  # Categoria do produto
  
  # Associa o gerenciador personalizado ao modelo Product
  objects = ProductManager()

# views.py
# Consulta produtos caros e, em seguida, filtra os da categoria 'Electronics'
expensive_electronics = Product.objects.get_expensive_products().get_filtered_products('Electronics')
