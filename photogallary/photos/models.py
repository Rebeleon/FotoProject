from __future__ import unicode_literals
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=250)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    likes = models.IntegerField(verbose_name='Нравится', default=0)
    dislikes = models.IntegerField(verbose_name='Не нравится', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

