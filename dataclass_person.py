from dataclasses import dataclass, field

@dataclass
class Person:
  name: str 
  quantity: int = field(repr=False)
  