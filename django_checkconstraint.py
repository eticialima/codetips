from django.db import models

# Modelo que representa um produto no banco de dados
class Product(models.Model):
  # Campo de nome do produto, com limite de 100 caracteres
  name = models.CharField(max_length=100)
  
  # Campo de preço, com até 10 dígitos, sendo 2 após a vírgula
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  # Campo booleano que indica se o produto está publicado ou não, padrão é False
  is_publish = models.BooleanField(default=False)
  
  # Definições adicionais para o modelo
  class Meta:
      # Restrições a serem aplicadas no banco de dados
      constraints = [
          # Restringe o preço a ser maior ou igual a 0 (não pode ser negativo)
          models.CheckConstraint(
            check=models.Q(price__gte=0), name="valid_price"
          ),
          # Permite que produtos com preço negativo ou zero só sejam salvos se não estiverem publicados
          models.CheckConstraint(
            check=models.Q(price__gte=0) | models.Q(is_published=False), 
            name="published_products_have_positive_price"
          ),
      ]



# exemple usage 

# Criando um produto com preço negativo e publicado
product = Product(name="Produto 3", price=-10.00, is_publish=True)

try:
    product.save()  # Isso resultará em um erro devido à constraint.
except Exception as e:
    print(e)  # Aqui será exibido um erro dizendo que não é permitido salvar o produto.
