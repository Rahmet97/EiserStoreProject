from django.db import models

class User(models.Model):
    sdm = models.CharField(max_length=255),
    dms = models.CharField(max_length=255),


# Create your models here.
