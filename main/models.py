from django.db import models


class CategoryProduct(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to=True)
    price = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=150)
class User(models.Model):
    sdm = models.CharField(max_length=255),
    dms = models.CharField(max_length=255),


# Create your models here.
