from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to='pics')
    price = models.FloatField()
    description = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=150)


class ShopCategory(models.Model):
    name = models.CharField(max_length=150)
class User(models.Model):
    sdm = models.CharField(max_length=255),
    dms = models.CharField(max_length=255),


# Create your models here.
