from dataclasses import dataclass

# A classe Color é imutável (congelada) devido ao uso do parâmetro frozen=True
@dataclass(frozen=True)
class Color:
  name: str
  hex_value: str
  
# Cria uma instância da classe Color com os valores 'red' e '#FF80000'
color = Color('red', '#FF80000')
