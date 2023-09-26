from django.db import models

class User(models.Model):
    sdm = models.CharField(max_length=255),
    dms = models.CharField(max_length=255),


class Product(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to=True)
    price = models.IntegerField()


class ShopCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    data = models.DateField(auto_now_add=True)