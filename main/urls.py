from django.urls import path

from .views import CategoryView, home, SingleProductView

urlpatterns = [
    path('category', CategoryView.as_view(), name='category'),
    path('', home),
    path('product/<int:id>', SingleProductView.as_view(), name='product'),
]
