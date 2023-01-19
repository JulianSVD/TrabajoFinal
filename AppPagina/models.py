from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField()
    intro =  models.TextField()
    cuerpo = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-date_added"]
    
