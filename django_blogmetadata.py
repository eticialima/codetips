from django.db import models
from django.db.models import Q

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    metadata = models.JSONField()

# Exemplo de dados de metadados para um post do blog
metadata = {
    'tags': ['technology', 'development'],
    'author_social': {
        'twitter': '@leticialimacgi',
        'github': '@eticialima'
    }
}

# Criação de um post
blog_post = BlogPost.objects.create(
    title='My first blog post',
    content='This is my first blog post',
    metadata=metadata
)

# Recuperar um post específico
blog_post = BlogPost.objects.get(pk=1)

# Acessar as tags e o twitter do autor
tags = blog_post.metadata.get('tags', [])
author_twitter = blog_post.metadata.get('author_social', {}).get('twitter', '')

# Consulta customizada com filtros nos metadados
custom_query = BlogPost.objects.filter(
    Q(metadata__tags__contains='development') & 
    Q(metadata__author_social__twitter='@leticialimacgi')
)
