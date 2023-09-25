from django.db import models


class CategoryProduct(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to='pics')
    price = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=150)
