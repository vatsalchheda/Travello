from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    off = models.BooleanField(default=False)


class Blogs(models.Model):
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
