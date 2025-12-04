from django.db import models

# Create your models here.

class CreateBlog(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    