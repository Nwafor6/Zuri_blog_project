from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length= 200)
    etxt=models.TextField()
    author= models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    created_date= models.DateTimeField()
    published_date= models.DateTimeField()

    def __str__(self):
        return self.title
