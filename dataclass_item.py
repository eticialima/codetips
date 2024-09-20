from dataclasses import dataclass, field

@dataclass
class Item:
  name: str
  price: float = 9.99
  quantity: int = field(default=1)
  

# Criando uma instância de Item com valores padrão
item1 = Item(name='Laptop')

# Criando uma instância de Item com valores personalizados
item2 = Item(name='Mouse', price=19.99, quantity=3)

# Acessando os atributos das instâncias
print(item1.name)      # Saída: Laptop
print(item1.price)     # Saída: 9.99 (valor padrão)
print(item1.quantity)  # Saída: 1 (valor padrão)

print(item2.name)      # Saída: Mouse
print(item2.price)     # Saída: 19.99
print(item2.quantity)  # Saída: 3
