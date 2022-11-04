from django.db import models
from users.models import User
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True) 

    def __str__(self):
        return str(self.content)
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    contant = models.TextField()
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return str(self.title)