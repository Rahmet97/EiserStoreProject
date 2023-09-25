from django.db import models


class User(models.Model):
    sdm = models.CharField(max_length=255),
    dms = models.CharField(max_length=255),


class Newsletter(models.Model):
    email = models.EmailField(max_length=50, verbose_name=('email'))

    def __str__(self):
        return self.email


class Comment(models.Model):
    message = models.TextField(max_length=100, verbose_name='message')
    name = models.CharField(max_length=50, verbose_name=('name'))
    email = models.EmailField(max_length=50, verbose_name=('email'))
    subject = models.CharField(max_length=50, verbose_name=('subject'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Comment')
        verbose_name_plural = ('Comments')
