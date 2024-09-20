# Tentativa inicial de criar uma classe usando o dataclass
from dataclasses import dataclass

@dataclass
class Point:
  x: int  # Coordenada X do ponto
  y: int  # Coordenada Y do ponto
  
# Redefinição manual da classe Point, sobrescrevendo a versão do dataclass anterior
class Point:
  # Inicializa um objeto Point com as coordenadas X e Y
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y
  
  # Representação em string para facilitar a exibição do objeto Point
  def __repr__(self) -> str:
    return f"Point(x={self.x}, y={self.y})"
  
  # Sobrescreve o comportamento de igualdade entre objetos Point
  def __eq__(self, value: object) -> bool:
    # Verifica se os valores das coordenadas X e Y dos dois pontos são iguais
    return (self.x, self.y) == (value.x, value.y)
