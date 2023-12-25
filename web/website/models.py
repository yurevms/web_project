from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20)
    text_data = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photos')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name