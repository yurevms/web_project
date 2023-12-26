from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20)
    text_data = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name

class Comments(models.Model):
    email = models.EmailField()
    yourname = models.CharField(max_length=50)
    text_comment = models.CharField(max_length=300)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name},{self.post}'