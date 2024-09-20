from django.db import models

# Basic model
class Product(models.Model):
    name =  models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
# Custom Behavior with proxy model 
class DiscountedProduct(Product):
    class Meta:
        ordering = ['price']
        proxy = True
        
    def discounted_price(self, discounted_percentage):
        return self.price * (1 - discounted_percentage / 100)
    
# Exemplo de usage
product = Product.objects.create(name='Labtop', price=1000.00)
discounted_product  = DiscountedProduct.objects.get(pk=product.pk)
discounted_price =  discounted_product.discounted_price(10) # 10% de desconto