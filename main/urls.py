from django.urls import path
from django.urls import path

from .views import home, cart

urlpatterns =[
    path('', home),
    path('cart', cart),
]