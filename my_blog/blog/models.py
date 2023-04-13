from django.db import models


class Post(models.Model):
    """post info"""
    title = models.CharField('Post title', max_length=150)
    description = models.TextField('Enter your text')
    author = models.CharField('Author', max_length=100)
    date = models.DateField('Date published')

    def __str__(self):
        return f'{self.title}, {self.author}'
