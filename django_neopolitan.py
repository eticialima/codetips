# Para usar o **Neapolitan** em projetos Django, que oferece views CRUD reutilizáveis, siga os passos abaixo:

# 1. **Instalação**:
# Instale o pacote Neapolitan com `pip`:
# pip install django-neapolitan

# 2. **Configuração**:
# No arquivo `settings.py` do seu projeto, adicione `'neapolitan'` à lista de `INSTALLED_APPS`:
INSTALLED_APPS = [
    # outras apps
    'neapolitan',
]

# 3. **Criação de Views CRUD**:
# Depois de configurar, você pode usar as views CRUD que o **Neapolitan** fornece para modelos do seu projeto. Por exemplo, vamos configurar um CRUD para um modelo `Book`.

# Exemplo:

# 1. **Modelo (models.py)**:
#    Crie um modelo no seu app:

from django.db import models

class Book(models.Model):
      title = models.CharField(max_length=200)
      author = models.CharField(max_length=100)
      published_date = models.DateField()

      def __str__(self):
         return self.title


# 2. **URLs (urls.py)**:
    # Use as views CRUD automáticas do Neapolitan nas suas URLs:

from django.urls import path
from neapolitan.views import CRUDView
from .models import Book

urlpatterns = [
   path('books/', CRUDView.as_view(model=Book), name='book_crud'),
]


# 4. **Acessando as Views**:
    # Agora, você terá automaticamente as páginas de lista, criação, edição e exclusão de `Book` na URL `/books/`, sem a necessidade de criar views individuais.

# 5. **Customização**:
    # Você pode personalizar templates e funções, como adicionar permissões ou modificar a aparência, se necessário.

# Com isso, o Neapolitan facilita a implementação rápida de funcionalidades CRUD para seus modelos Django.
