from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

     #This changes the title ofthe object returned in the admin page
    def __str__(self):
        return self.text[:50]
