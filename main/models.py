from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to='pics')
    price = models.FloatField()
    discription = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=150)


class ShopCategory(models.Model):
    name = models.CharField(max_length=150)
