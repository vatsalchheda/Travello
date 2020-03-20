from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    off = models.BooleanField(default=False)


class Blog(models.Model):
    Title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    content = models.TextField()
