from django.db import models

# sem Abstract Base Class
class BlogPost(models.Model):
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)



# Com Abstract Base Class
class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  
class BlogPost(TimestampedModel):
  title = models.CharField(max_length=100) 
  
class Comment(TimestampedModel):
  content = models.TextField() 