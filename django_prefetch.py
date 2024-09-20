from django.db import models

class Tag(models.Model):
  name = models.CharField(max_length=255)
  
class Article(models.Model):
  title =  models.CharField(max_length=255)
  tags = models.ManyToManyField(Tag)
  
  
# views.py
articles = Article.objects.prefetch_related('tags')


## Solução 2 
from django.db.models import Prefetch
from .models import Author

# Prefetch
authors = Author.objects.prefetch_related(
  Prefetch('books', queryset=Book.objects.filter(title__contains="Django"))
)