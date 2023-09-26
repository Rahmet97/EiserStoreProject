from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    images = models.ImageField(upload_to='pics')
    price = models.FloatField()
    description = models.TextField()
    uploaded_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=150)


class User(models.Model):
    sdm = models.CharField(max_length=255),
    dms = models.CharField(max_length=255),


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Comment(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    website = models.URLField(blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text
