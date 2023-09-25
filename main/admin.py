from django.contrib import admin
from django.contrib.admin import site
from .models import Newsletter, Comment

# Register your models here.
admin = site.register((Newsletter, Comment))
