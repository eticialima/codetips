from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Product, Order, Customer  # Importa os modelos relevantes
from .serializers import OrderSerializer  # Importa o serializer para a Order

# Classe de view para processar uma nova ordem de compra
class ProcessOrderView(generics.CreateAPIView):
  # Define o serializer que será usado para criar a ordem
  serializer_class = OrderSerializer
  
  # Método que é chamado automaticamente ao criar uma nova ordem
  def perform_create(self, serializer):
    try:
      # Inicia uma transação atômica, garantindo que todas as operações dentro dela sejam concluídas
      # ou nenhuma será aplicada em caso de erro
      with transaction.atomic():
        # Salva a ordem com o status 'Processing'
        order = serializer.save(status='Processing')
        
        # Itera sobre todos os itens associados à ordem
        for item in order.items.all():
          product = item.product  # Obtém o produto correspondente ao item
          
          # Verifica se há estoque suficiente para o produto
          if product.stock < item.quantity:
            # Se não houver estoque suficiente, levanta uma exceção de validação
            raise ValidationError(f'Not enough stock for {product.name}')
          
          # Reduz o estoque do produto com base na quantidade pedida
          product.stock -= item.quantity
          product.save()  # Salva o novo estado do produto
          
        # Atualiza o status da ordem para 'Completed' após processar todos os itens
        order.status = 'Completed'
        order.save()  # Salva a ordem com o status atualizado
    
    # Captura e relança a exceção de validação em caso de erro
    except ValidationError as e:
      raise e
