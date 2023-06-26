
from pyexpat import model
from django.db import models
from django.conf import settings
from django.urls import reverse


USER = settings.AUTH_USER_MODEL
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})
    


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article-list')