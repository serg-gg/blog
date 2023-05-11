from django.db import models


class Post(models.Model):
    title = models.CharField('Post title', max_length=150)
    description = models.TextField('Enter your text')
    author = models.CharField('Author', max_length=100)
    date = models.DateField('Date published')
    img = models.ImageField('Image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

class Likes(models.Model):
    ip = models.CharField('IP-address', max_length=20)
    pos = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

