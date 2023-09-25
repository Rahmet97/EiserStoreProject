from django.urls import path

<<<<<<< HEAD
from .views import CategoryView, home, S

urlpatterns = [
    path('category', CategoryView.as_view, name='category'),
    path('', home),
    path('single-product', )
]
=======
from .views import CategoryView, home

urlpatterns = [
    path('', home, name='home'),
    path('category', CategoryView.as_view(), name='category')
]

>>>>>>> 98e01cabc0cfa903ca2c3307893894a4b7556e89
