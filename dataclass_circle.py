from dataclasses import dataclass

# A classe Circle usa a função dataclass para simplificar a criação de classes
@dataclass
class Circle:
  radius: float
  area: float = 0.0
  
  # Método especial que é chamado após a inicialização do dataclass
  def __post_init__(self):
    # Calcula a área do círculo usando a fórmula π * raio² e atribui ao atributo 'area'
    self.area = 3.1415 * self.radius ** 2
