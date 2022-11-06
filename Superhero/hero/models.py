
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class Superhero(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200,)
    description = models.TextField(default="None")
    image = models.CharField(max_length=200, default="None")
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, default = '69')

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200, default="None")
    body = models.TextField(default="None")
    image = models.CharField(max_length=200, default="None")
    investigator = models.ForeignKey(
        User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article_list')
