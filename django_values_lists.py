from django.db import models

# Modelo que representa um livro
class Book(models.Model):
  title = models.CharField(max_length=200)  # Título do livro
  author = models.ForeignKey('Author', on_delete=models.CASCADE)  # Referência ao autor (relacionamento de chave estrangeira)
  pages = models.IntegerField()  # Número de páginas do livro
  
  # Método que define a representação em string do objeto Book
  def __str__(self) -> str:
    return self.title  # Retorna o título do livro como string

# Modelo que representa um autor
class Author(models.Model):
  name = models.CharField(max_length=200)  # Nome do autor
  
  # Método que define a representação em string do objeto Author
  def __str__(self) -> str:
    return self.name  # Retorna o nome do autor como string

  
# views.py 
# Consulta usando select_related para otimizar a busca do autor de cada livro
# Retorna um dicionário (dict) com o título do livro e o nome do autor
books = Book.objects.select_related('author').values('title', 'author__name')

# Outra consulta semelhante, mas retorna uma lista de tuplas (list) com o título e o nome do autor
books = Book.objects.select_related('author').values_list('title', 'author__name')
